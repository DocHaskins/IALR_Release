#!/usr/bin/env python3
"""
JSON Sync Tool
==============
Validates and synchronizes JSON configuration files against a base template.

Usage:
    python json_sync_tool.py <json_filename> [--dry-run] [--verbose]
    python json_sync_tool.py modules.json --dry-run
    python json_sync_tool.py pathways.json --verbose
    python json_sync_tool.py --all --dry-run

The base JSON files should be in the same directory as this script.
The tool searches all subdirectories for JSON files with the same name.

The tool will:
1. Load the base JSON file (from script directory) as the source of truth
2. Search all subdirectories for JSON files with the same name
3. Match entries by "name" field and update with full formatting from base
4. Report entries that don't exist in the base file
5. Optionally write the corrected files back
"""

import json
import os
import sys
import argparse
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ValidationResult:
    """Holds the results of validating a single JSON file."""
    file_path: str
    root_key: str = ""
    updated_entries: list = field(default_factory=list)
    missing_from_base: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    was_modified: bool = False


@dataclass 
class SyncReport:
    """Overall report for all processed files."""
    base_file: str
    search_directory: str
    files_processed: int = 0
    files_modified: int = 0
    total_entries_updated: int = 0
    total_missing_entries: int = 0
    results: list = field(default_factory=list)


def load_json_file(file_path: str) -> dict | None:
    """Load and parse a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON parse error in {file_path}: {e}")
        return None
    except Exception as e:
        print(f"  ❌ Error reading {file_path}: {e}")
        return None


def save_json_file(file_path: str, data: dict, indent: int = 4) -> bool:
    """Save data to a JSON file with proper formatting."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
            f.write('\n')  # Add trailing newline
        return True
    except Exception as e:
        print(f"  ❌ Error writing {file_path}: {e}")
        return False


def normalize_name(name: str) -> str:
    """
    Normalize a name for comparison purposes.
    Handles variations like 'RoadWarrior' vs 'Road Warrior', 
    'No Kid Infected' vs 'Remove Child Infected', etc.
    """
    # Convert to lowercase and remove spaces/underscores for comparison
    normalized = name.lower().replace(' ', '').replace('_', '').replace('-', '')
    return normalized


# Known aliases for name variations that can't be matched automatically
# Format: 'variant_name_normalized': 'base_name_normalized'
DEFAULT_ALIASES = {
    'nokidinfected': 'removechildinfected',
    'nokids': 'removechildinfected', 
    'nochildinfected': 'removechildinfected',
    'volatilesbegone': 'volatilesbegone',
    'volibegone': 'volatilesbegone',
    'roadwarrior': 'roadwarrior',
    'doomsdayprepper': 'doomsdayprepper',
}


def load_aliases(alias_file: str = None) -> dict:
    """Load custom aliases from a JSON file if provided."""
    aliases = DEFAULT_ALIASES.copy()
    
    if alias_file and os.path.isfile(alias_file):
        try:
            with open(alias_file, 'r') as f:
                custom_aliases = json.load(f)
                # Normalize all keys and values
                for k, v in custom_aliases.items():
                    aliases[normalize_name(k)] = normalize_name(v)
        except Exception as e:
            print(f"  ⚠ Warning: Could not load aliases from {alias_file}: {e}")
    
    return aliases


def build_base_lookup(base_data: dict, root_key: str) -> dict:
    """
    Build a lookup dictionary from base data.
    Returns dict mapping normalized names to full entry data.
    """
    lookup = {}
    entries = base_data.get(root_key, [])
    
    for entry in entries:
        if 'name' in entry:
            # Store both normalized and original name mappings
            norm_name = normalize_name(entry['name'])
            lookup[norm_name] = entry
            # Also store exact match
            lookup[entry['name'].lower()] = entry
    
    return lookup


def find_matching_entry(name: str, base_lookup: dict, aliases: dict = None) -> dict | None:
    """
    Find a matching entry in the base lookup.
    Tries exact match first, then normalized match, then aliases.
    """
    if aliases is None:
        aliases = DEFAULT_ALIASES
    
    # Try exact lowercase match
    if name.lower() in base_lookup:
        return base_lookup[name.lower()]
    
    # Try normalized match
    norm_name = normalize_name(name)
    if norm_name in base_lookup:
        return base_lookup[norm_name]
    
    # Try alias match
    if norm_name in aliases:
        alias_target = aliases[norm_name]
        if alias_target in base_lookup:
            return base_lookup[alias_target]
    
    # Try partial matching for common variations
    for key, entry in base_lookup.items():
        if norm_name in key or key in norm_name:
            return entry
    
    return None


def sync_json_file(
    target_path: str,
    base_lookup: dict,
    root_key: str,
    aliases: dict = None,
    dry_run: bool = False,
    verbose: bool = False
) -> ValidationResult:
    """
    Synchronize a target JSON file against the base lookup.
    """
    result = ValidationResult(file_path=target_path, root_key=root_key)
    
    if aliases is None:
        aliases = DEFAULT_ALIASES
    
    # Load target file
    target_data = load_json_file(target_path)
    if target_data is None:
        result.errors.append("Failed to load JSON file")
        return result
    
    # Check if root key exists
    if root_key not in target_data:
        result.errors.append(f"Root key '{root_key}' not found in file")
        return result
    
    entries = target_data[root_key]
    updated_entries = []
    
    for entry in entries:
        if 'name' not in entry:
            result.errors.append(f"Entry without 'name' field found: {entry}")
            updated_entries.append(entry)
            continue
        
        entry_name = entry['name']
        base_entry = find_matching_entry(entry_name, base_lookup, aliases)
        
        if base_entry:
            # Found match - use the base entry (fully formatted)
            if verbose:
                print(f"    ✓ Matched: '{entry_name}' → '{base_entry['name']}'")
            result.updated_entries.append({
                'original_name': entry_name,
                'base_name': base_entry['name'],
                'fields_added': [k for k in base_entry.keys() if k not in entry]
            })
            updated_entries.append(base_entry.copy())
            result.was_modified = True
        else:
            # No match found - keep original and report
            if verbose:
                print(f"    ⚠ Not in base: '{entry_name}'")
            result.missing_from_base.append(entry_name)
            updated_entries.append(entry)
    
    # Update the data
    target_data[root_key] = updated_entries
    
    # Write back if not dry run and file was modified
    if not dry_run and result.was_modified:
        if save_json_file(target_path, target_data):
            if verbose:
                print(f"    💾 Saved updated file")
        else:
            result.errors.append("Failed to save updated file")
    
    return result


def find_json_files(search_dir: str, filename: str) -> list[str]:
    """
    Find all JSON files with the given filename in subdirectories only.
    Does not include files in the root search_dir itself.
    """
    found_files = []
    search_path = Path(search_dir)
    
    for json_file in search_path.rglob(filename):
        # Skip files in the root directory (those are base files)
        if json_file.parent != search_path:
            found_files.append(str(json_file))
    
    return sorted(found_files)


def detect_root_key(data: dict) -> str | None:
    """
    Detect the root key of the JSON structure.
    Looks for common patterns like 'modules', 'pathways', etc.
    """
    for key, value in data.items():
        if isinstance(value, list) and len(value) > 0:
            if isinstance(value[0], dict) and 'name' in value[0]:
                return key
    return None


def run_sync(
    base_json_path: str,
    search_directory: str,
    alias_file: str = None,
    dry_run: bool = False,
    verbose: bool = False
) -> SyncReport:
    """
    Main synchronization function.
    """
    report = SyncReport(
        base_file=base_json_path,
        search_directory=search_directory
    )
    
    # Load aliases
    aliases = load_aliases(alias_file)
    
    # Load base JSON
    print(f"\n📂 Loading base file: {base_json_path}")
    base_data = load_json_file(base_json_path)
    if base_data is None:
        print("❌ Failed to load base JSON file")
        return report
    
    # Detect root key
    root_key = detect_root_key(base_data)
    if root_key is None:
        print("❌ Could not detect root key in base JSON")
        return report
    
    print(f"   Root key detected: '{root_key}'")
    print(f"   Entries in base: {len(base_data[root_key])}")
    
    # Build lookup
    base_lookup = build_base_lookup(base_data, root_key)
    print(f"   Lookup entries created: {len(base_lookup)}")
    print(f"   Aliases loaded: {len(aliases)}")
    
    # Get the filename to search for
    base_filename = Path(base_json_path).name
    
    # Find all matching JSON files in subdirectories
    print(f"\n🔍 Searching subdirectories for '{base_filename}'...")
    target_files = find_json_files(search_directory, base_filename)
    
    print(f"   Found {len(target_files)} file(s) to process")
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - No files will be modified\n")
    
    # Process each file
    for target_path in target_files:
        print(f"\n📄 Processing: {target_path}")
        result = sync_json_file(
            target_path=target_path,
            base_lookup=base_lookup,
            root_key=root_key,
            aliases=aliases,
            dry_run=dry_run,
            verbose=verbose
        )
        
        report.results.append(result)
        report.files_processed += 1
        
        if result.was_modified:
            report.files_modified += 1
        
        report.total_entries_updated += len(result.updated_entries)
        report.total_missing_entries += len(result.missing_from_base)
        
        # Print summary for this file
        if result.updated_entries:
            print(f"   ✓ Updated {len(result.updated_entries)} entries")
        if result.missing_from_base:
            print(f"   ⚠ Missing from base: {len(result.missing_from_base)} entries")
            for name in result.missing_from_base:
                print(f"      - {name}")
        if result.errors:
            print(f"   ❌ Errors: {len(result.errors)}")
            for error in result.errors:
                print(f"      - {error}")
    
    return report


def print_final_report(report: SyncReport):
    """Print the final summary report."""
    print("\n" + "=" * 60)
    print("📊 SYNC REPORT")
    print("=" * 60)
    print(f"Base file: {report.base_file}")
    print(f"Search directory: {report.search_directory}")
    print(f"Files processed: {report.files_processed}")
    print(f"Files modified: {report.files_modified}")
    print(f"Total entries updated: {report.total_entries_updated}")
    print(f"Total entries missing from base: {report.total_missing_entries}")
    
    # Collect all missing entries across all files
    all_missing = []
    for result in report.results:
        for name in result.missing_from_base:
            all_missing.append((result.file_path, name))
    
    if all_missing:
        print("\n⚠️  ENTRIES NOT IN BASE (need manual addition):")
        print("-" * 40)
        for file_path, name in all_missing:
            print(f"   [{Path(file_path).parent.name}] {name}")
    
    print("\n" + "=" * 60)


def get_script_directory() -> Path:
    """Get the directory where this script is located."""
    return Path(__file__).parent.resolve()


def get_syncable_json_files(script_dir: Path) -> list[str]:
    """
    Find JSON files in the script directory that can be synced.
    These are JSON files that have a list with 'name' fields.
    """
    syncable = []
    for json_file in script_dir.glob("*.json"):
        try:
            data = load_json_file(str(json_file))
            if data and detect_root_key(data):
                syncable.append(json_file.name)
        except:
            pass
    return sorted(syncable)


def main():
    parser = argparse.ArgumentParser(
        description="Sync JSON configuration files against a base template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python json_sync_tool.py modules.json --dry-run
  python json_sync_tool.py pathways.json --verbose
  python json_sync_tool.py difficulties.json
  python json_sync_tool.py --all --dry-run
  python json_sync_tool.py --list
        """
    )
    
    parser.add_argument(
        'json_file',
        nargs='?',
        help='Name of the JSON file to sync (e.g., modules.json, pathways.json)'
    )
    
    parser.add_argument(
        '--all', '-A',
        action='store_true',
        help='Sync all detected JSON files in the script directory'
    )
    
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List all syncable JSON files found in script directory'
    )
    
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output for each entry processed'
    )
    
    parser.add_argument(
        '--aliases', '-a',
        help='Path to custom aliases JSON file for name mappings'
    )
    
    args = parser.parse_args()
    
    # Get script directory
    script_dir = get_script_directory()
    print(f"📁 Script directory: {script_dir}")
    
    # List mode
    if args.list:
        syncable = get_syncable_json_files(script_dir)
        if syncable:
            print(f"\n📋 Syncable JSON files found:")
            for f in syncable:
                print(f"   • {f}")
        else:
            print("\n⚠️  No syncable JSON files found in script directory")
        sys.exit(0)
    
    # Determine which files to process
    if args.all:
        json_files = get_syncable_json_files(script_dir)
        if not json_files:
            print("❌ No syncable JSON files found")
            sys.exit(1)
    elif args.json_file:
        json_files = [args.json_file]
    else:
        parser.print_help()
        print("\n❌ Please specify a JSON file or use --all")
        sys.exit(1)
    
    # Process each JSON file
    total_missing = 0
    for json_filename in json_files:
        base_path = script_dir / json_filename
        
        if not base_path.is_file():
            print(f"❌ Base JSON file not found: {base_path}")
            continue
        
        # Run sync
        report = run_sync(
            base_json_path=str(base_path),
            search_directory=str(script_dir),
            alias_file=args.aliases,
            dry_run=args.dry_run,
            verbose=args.verbose
        )
        
        # Print final report
        print_final_report(report)
        total_missing += report.total_missing_entries
    
    # Exit with error code if there were missing entries
    if total_missing > 0:
        sys.exit(2)
    
    sys.exit(0)


if __name__ == '__main__':
    main()
