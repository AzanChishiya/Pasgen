#!/usr/bin/env python3
"""
pasgen - Targeted Password Wordlist Generator
Author: Inspired by your ideas
Version: 1.1 (Super Fast)
"""

import os
import sys
import time
import itertools
from pathlib import Path

# --- Stylish output helpers (ANSI colors) ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ██████╗  █████╗ ███████╗ ██████╗ ███████╗███╗   ██╗  ║
║   ██╔══██╗██╔══██╗██╔════╝██╔════╝ ██╔════╝████╗  ██║  ║
║   ██████╔╝███████║███████╗██║  ███╗█████╗  ██╔██╗ ██║  ║
║   ██╔═══╝ ██╔══██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║  ║
║   ██║     ██║  ██║███████║╚██████╔╝███████╗██║ ╚████║  ║
║   ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝  ║
║                                                          ║
║              Targeted Password Wordlist Generator        ║
║                      {Colors.YELLOW}pasgen v1.1{Colors.CYAN}                           ║
╚══════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(banner)

def print_info(msg):
    print(f"{Colors.GREEN}[*]{Colors.END} {msg}")

def print_input(msg):
    return input(f"{Colors.YELLOW}[?]{Colors.END} {msg}")

def print_success(msg):
    print(f"{Colors.BLUE}[+]{Colors.END} {msg}")

def print_error(msg):
    print(f"{Colors.RED}[!]{Colors.END} {msg}")

# --- Core generation functions (optimized) ---

def apply_case(word, case_style):
    if case_style == 'upper':
        return word.upper()
    elif case_style == 'lower':
        return word.lower()
    elif case_style == 'capitalize':
        return word.capitalize()
    return word

def generate_variants(name, case_styles):
    variants = set()
    for style in case_styles:
        variants.add(apply_case(name, style))
    return list(variants)

def estimate_total(names, numbers, symbols, case_styles):
    """Calculate total number of combinations without generating them."""
    name_variants = []
    for name in names:
        name_variants.extend(generate_variants(name, case_styles))
    num_strings = list(map(str, numbers))
    sym_list = list(symbols)
    
    total = 0
    # Patterns with symbol + number
    if sym_list and num_strings:
        total += 4 * len(name_variants) * len(sym_list) * len(num_strings)  # patterns 1-4
    # Pattern 5: name + num
    if num_strings:
        total += len(name_variants) * len(num_strings)
    # Pattern 6: name + sym
    if sym_list:
        total += len(name_variants) * len(sym_list)
    return total

def generate_passwords(names, numbers, symbols, case_styles):
    """Yield passwords using itertools.product for maximum speed."""
    # Precompute all name variants
    name_variants = []
    for name in names:
        name_variants.extend(generate_variants(name, case_styles))
    
    # Convert numbers to strings once
    num_strings = [str(num) for num in numbers]
    sym_list = list(symbols)
    
    # Pattern 1: name + sym + num
    for name, sym, num in itertools.product(name_variants, sym_list, num_strings):
        yield f"{name}{sym}{num}"
    
    # Pattern 2: name + num + sym
    for name, num, sym in itertools.product(name_variants, num_strings, sym_list):
        yield f"{name}{num}{sym}"
    
    # Pattern 3: num + name + sym
    for num, name, sym in itertools.product(num_strings, name_variants, sym_list):
        yield f"{num}{name}{sym}"
    
    # Pattern 4: sym + name + num
    for sym, name, num in itertools.product(sym_list, name_variants, num_strings):
        yield f"{sym}{name}{num}"
    
    # Pattern 5: name + num
    for name, num in itertools.product(name_variants, num_strings):
        yield f"{name}{num}"
    
    # Pattern 6: name + sym
    for name, sym in itertools.product(name_variants, sym_list):
        yield f"{name}{sym}"

def main():
    print_banner()
    print_info("Welcome to pasgen – your personal password wordlist generator!")
    print_info("Let's set up your target parameters.\n")

    # --- Collect user inputs ---
    names_input = print_input("Enter names (comma-separated, e.g., Qamar, Ubaid): ")
    names = [n.strip() for n in names_input.split(',') if n.strip()]
    if not names:
        print_error("No names provided. Exiting.")
        sys.exit(1)

    # Number range
    try:
        start_num = int(print_input("Enter start number (e.g., 0): "))
        end_num = int(print_input("Enter end number (e.g., 9999): "))
        if start_num > end_num:
            print_error("Start number cannot be greater than end number.")
            sys.exit(1)
        numbers = list(range(start_num, end_num + 1))
    except ValueError:
        print_error("Invalid number input. Please enter integers.")
        sys.exit(1)

    symbols_input = print_input("Enter symbols to use (e.g., @_-., no spaces): ")
    symbols = symbols_input.strip()

    # Case options
    print_info("\nChoose case styles (you can select multiple by comma, e.g., 1,2,3):")
    print("  1. ALL CAPS")
    print("  2. all lowercase")
    print("  3. First letter capitalized")
    case_choice = print_input("Enter numbers (1,2,3): ")
    case_map = {'1': 'upper', '2': 'lower', '3': 'capitalize'}
    selected = [case_map[c.strip()] for c in case_choice.split(',') if c.strip() in case_map]
    if not selected:
        print_error("No valid case style selected. Exiting.")
        sys.exit(1)

    # --- Estimate total combinations ---
    total_combos = estimate_total(names, numbers, symbols, selected)
    print_info(f"Estimated total passwords to generate: {total_combos:,}")
    if total_combos > 10_000_000:
        print_info("This is a large wordlist. Generation may take time and disk space.")
    
    # --- Generate wordlist with chunked writing for speed ---
    output_path = Path.home() / "Desktop" / "pasgen_wordlist.txt"
    print_info(f"\nGenerating passwords... saving to: {output_path}")
    start_time = time.time()

    try:
        # Use a large buffer and write in chunks
        chunk_size = 10000  # write 10k lines at a time
        chunk = []
        count = 0

        with open(output_path, 'w', encoding='utf-8', buffering=1024*1024) as f:
            for pwd in generate_passwords(names, numbers, symbols, selected):
                chunk.append(pwd + '\n')
                count += 1
                if len(chunk) >= chunk_size:
                    f.writelines(chunk)
                    chunk.clear()
                if count % 1_000_000 == 0:
                    elapsed = time.time() - start_time
                    print_info(f"Generated {count:,} passwords so far... ({elapsed:.1f}s elapsed)")
            
            # Write any remaining
            if chunk:
                f.writelines(chunk)
        
        elapsed = time.time() - start_time
        print_success(f"\nSuccess! Wordlist saved to: {output_path}")
        print_info(f"Total passwords generated: {count:,}")
        print_info(f"Time taken: {elapsed:.2f} seconds")

    except Exception as e:
        print_error(f"An error occurred while writing the file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
