import csv
import re
from collections import defaultdict

def process_qase_data(csv_file_path):
    suites = {}
    test_cases = []
    
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader) # Skip header

        # Find column indices dynamically
        try:
            v2_id_idx = header.index('v2.id')
            title_idx = header.index('title')
            suite_id_idx = header.index('suite_id')
            suite_title_idx = header.index('suite')
        except ValueError as e:
            print(f"Missing expected column in CSV: {e}")
            return None, None, None, None, None

        for row in reader:
            if not row:
                continue

            v2_id = row[v2_id_idx].strip() if v2_id_idx < len(row) else ''
            title = row[title_idx].strip() if title_idx < len(row) else ''
            suite_id = row[suite_id_idx].strip() if suite_id_idx < len(row) else ''
            suite_title = row[suite_title_idx].strip() if suite_title_idx < len(row) else ''

            # Collect suite information
            if suite_title and suite_id:
                if suite_id not in suites:
                    suites[suite_id] = {
                        'title': suite_title,
                        'first_word': re.match(r'\w+', suite_title).group(0).lower() if re.match(r'\w+', suite_title) else '',
                        'is_top_level': bool(re.match(r'^\d+\s', suite_title)),
                        'original_cases': [], 
                        'assigned_cases': []  
                    }

            # Collect test case information and populate original_cases for suites
            if v2_id and title:
                tc = {
                    'id': v2_id,
                    'title': title,
                    'first_word': re.match(r'\w+', title).group(0).lower() if re.match(r'\w+', title) else '',
                    'original_suite_id': suite_id,
                    'assigned_suite_id': None
                }
                test_cases.append(tc)
                if suite_id in suites:
                    suites[suite_id]['original_cases'].append(v2_id)

    # Calculate original average case count per non-top-level suite
    total_original_cases = 0
    non_top_level_suites_count = 0
    for s_id, s_info in suites.items():
        if not s_info['is_top_level']:
            total_original_cases += len(s_info['original_cases'])
            non_top_level_suites_count += 1
    original_avg_cases_per_suite = total_original_cases / non_top_level_suites_count if non_top_level_suites_count > 0 else 0

    # Initialize assigned_cases based on original assignments for non-top-level suites
    unassigned_test_cases_initial = []
    for tc in test_cases:
        original_suite_id = tc['original_suite_id']
        if original_suite_id and original_suite_id in suites and not suites[original_suite_id]['is_top_level']:
            tc['assigned_suite_id'] = original_suite_id
            suites[original_suite_id]['assigned_cases'].append(tc['id'])
        else:
            # These are cases that are originally in a top-level suite (or no suite), they need reassignment
            unassigned_test_cases_initial.append(tc)

    # Group non-top-level suites by their first word for efficient lookup (only for reassignment pool)
    suites_by_first_word = defaultdict(list)
    for suite_id, suite_info in suites.items():
        if not suite_info['is_top_level']:
            suites_by_first_word[suite_info['first_word']].append(suite_id)

    # Now, try to assign the initially unassigned test cases using enhanced matching and load balancing
    unassigned_after_reassignment = []
    for tc in unassigned_test_cases_initial:
        assigned = False
        tc_first_word = tc['first_word']

        if tc_first_word in suites_by_first_word:
            candidate_suite_ids = suites_by_first_word[tc_first_word]
            
            best_suite_id = None
            min_assigned_cases = float('inf')
            
            for s_id in candidate_suite_ids:
                if not suites[s_id]['is_top_level']:
                    # Try to use original suite if it's a non-top-level candidate, otherwise pick least loaded
                    if tc['original_suite_id'] == s_id:
                        best_suite_id = s_id
                        break
                    if len(suites[s_id]['assigned_cases']) < min_assigned_cases:
                        min_assigned_cases = len(suites[s_id]['assigned_cases'])
                        best_suite_id = s_id
            
            if best_suite_id:
                tc['assigned_suite_id'] = best_suite_id
                suites[best_suite_id]['assigned_cases'].append(tc['id'])
                assigned = True
        
        if not assigned:
            unassigned_after_reassignment.append(tc)

    # Calculate new average case count per non-top-level suite
    total_assigned_cases = 0
    non_top_level_suites_with_cases_count = 0
    for s_id, s_info in suites.items():
        if not s_info['is_top_level']:
            total_assigned_cases += len(s_info['assigned_cases'])
            if len(s_info['assigned_cases']) > 0:
                non_top_level_suites_with_cases_count += 1
    new_avg_cases_per_suite = total_assigned_cases / non_top_level_suites_with_cases_count if non_top_level_suites_with_cases_count > 0 else 0

    return suites, test_cases, unassigned_after_reassignment, original_avg_cases_per_suite, new_avg_cases_per_suite

if __name__ == "__main__":
    csv_file = "QD-2026-02-13.csv"
    suites_data, test_cases_data, unassigned_cases, original_avg, new_avg = process_qase_data(csv_file)

    if suites_data and test_cases_data:
        print("\n--- Suite Reorganization Results ---")
        print(f"Original Average Cases per Non-Top-Level Suite: {original_avg:.2f}")
        print(f"New Average Cases per Non-Top-Level Suite: {new_avg:.2f}")
        print("\nAssigned Suites Overview:")
        for s_id, s_info in suites_data.items():
            if not s_info['is_top_level']:
                print(f"  Suite ID: {s_id}, Title: {s_info['title']}, First Word: {s_info['first_word']}")
                print(f"    Original Cases: {len(s_info['original_cases'])}")
                print(f"    Assigned Cases: {len(s_info['assigned_cases'])}")
            else:
                print(f"  Top-Level Suite ID: {s_id}, Title: {s_info['title']}, First Word: {s_info['first_word']}")
                print(f"    Original Cases: {len(s_info['original_cases'])}")
                print(f"    Assigned Cases: {len(s_info['assigned_cases'])}")
                if len(s_info['assigned_cases']) > 0:
                    print("      WARNING: Top-level suite has assigned cases!")

        if unassigned_cases:
            print("\n--- Unassigned Test Cases (After Reassignment Attempt) ---")
            print("ID,Title,First Word,Original Suite ID")
            for tc in unassigned_cases:
                print(f"{tc['id']},{tc['title']},{tc['first_word']},{tc['original_suite_id']}")
        else:
            print("\nAll test cases have been assigned to an appropriate suite or remained in their original (non-top-level) suite.")

    else:
        print("Failed to process CSV data.")
