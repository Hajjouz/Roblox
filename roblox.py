#!/usr/bin/env python3
"""
Roblox Username Checker
A tool to check the availability and validity of Roblox usernames
"""

import requests
import time
import sys
from typing import Tuple, Optional

class RobloxUsernameChecker:
    """Check Roblox username availability and validity"""
    
    BASE_URL = "https://auth.roblox.com/v1/usernames/validate"
    USER_API = "https://api.roblox.com/users/get-by-username"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Content-Type': 'application/json'
        })
    
    def validate_username(self, username: str) -> Tuple[bool, str]:
        """
        Validate if a username meets Roblox requirements
        
        Args:
            username: The username to validate
            
        Returns:
            Tuple of (is_valid, message)
        """
        try:
            payload = {
                "username": username,
                "birthday": "1990-01-01T00:00:00.000Z"
            }
            
            response = self.session.post(
                self.BASE_URL,
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('code') == 0:
                    return True, "Username is valid and available! ✅"
                else:
                    return False, data.get('message', 'Username is not available')
            else:
                return False, f"API error: {response.status_code}"
                
        except requests.exceptions.Timeout:
            return False, "Request timeout - please try again"
        except requests.exceptions.RequestException as e:
            return False, f"Network error: {str(e)}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def check_username_exists(self, username: str) -> Tuple[bool, Optional[dict]]:
        """
        Check if a username already exists on Roblox
        
        Args:
            username: The username to check
            
        Returns:
            Tuple of (exists, user_data)
        """
        try:
            response = self.session.get(
                self.USER_API,
                params={'username': username},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'Id' in data:
                    return True, {
                        'id': data.get('Id'),
                        'username': data.get('Username'),
                        'created': 'User exists'
                    }
            
            return False, None
            
        except Exception as e:
            return False, None
    
    def check_bulk(self, usernames: list, delay: float = 0.5) -> dict:
        """
        Check multiple usernames
        
        Args:
            usernames: List of usernames to check
            delay: Delay between requests in seconds
            
        Returns:
            Dictionary with results
        """
        results = {
            'available': [],
            'taken': [],
            'invalid': []
        }
        
        total = len(usernames)
        
        for idx, username in enumerate(usernames, 1):
            print(f"\n[{idx}/{total}] Checking: {username}")
            
            # Check if username exists
            exists, user_data = self.check_username_exists(username)
            
            if exists:
                results['taken'].append({
                    'username': username,
                    'data': user_data
                })
                print(f"  ❌ Taken - User ID: {user_data['id']}")
            else:
                # Validate if available
                is_valid, message = self.validate_username(username)
                
                if is_valid:
                    results['available'].append(username)
                    print(f"  ✅ Available!")
                else:
                    results['invalid'].append({
                        'username': username,
                        'reason': message
                    })
                    print(f"  ⚠️  Invalid - {message}")
            
            # Rate limiting
            if idx < total:
                time.sleep(delay)
        
        return results


def print_banner():
    """Print application banner"""
    banner = """
╔═══════════════════════════════════════════════╗
║     ROBLOX USERNAME CHECKER                   ║
║     Check username availability & validity    ║
╚═══════════════════════════════════════════════╝
    """
    print(banner)


def print_results_summary(results: dict):
    """Print summary of results"""
    print("\n" + "="*50)
    print("📊 RESULTS SUMMARY")
    print("="*50)
    
    print(f"\n✅ Available: {len(results['available'])}")
    for username in results['available']:
        print(f"   - {username}")
    
    print(f"\n❌ Taken: {len(results['taken'])}")
    for item in results['taken']:
        print(f"   - {item['username']} (ID: {item['data']['id']})")
    
    print(f"\n⚠️  Invalid: {len(results['invalid'])}")
    for item in results['invalid']:
        print(f"   - {item['username']}: {item['reason']}")
    
    print("\n" + "="*50)


def main():
    """Main function"""
    print_banner()
    
    checker = RobloxUsernameChecker()
    
    print("\nMODE SELECTION:")
    print("1. Check single username")
    print("2. Check multiple usernames (bulk)")
    print("3. Check from file")
    
    choice = input("\nSelect mode (1-3): ").strip()
    
    if choice == "1":
        # Single username check
        username = input("\nEnter username to check: ").strip()
        
        if not username:
            print("❌ Username cannot be empty!")
            sys.exit(1)
        
        print(f"\n🔍 Checking username: {username}")
        print("-" * 50)
        
        # Check if exists
        exists, user_data = checker.check_username_exists(username)
        
        if exists:
            print(f"\n❌ USERNAME TAKEN")
            print(f"User ID: {user_data['id']}")
            print(f"Username: {user_data['username']}")
        else:
            # Validate availability
            is_valid, message = checker.validate_username(username)
            
            if is_valid:
                print(f"\n✅ USERNAME AVAILABLE!")
                print("This username can be registered on Roblox")
            else:
                print(f"\n⚠️  USERNAME INVALID")
                print(f"Reason: {message}")
    
    elif choice == "2":
        # Bulk check from input
        print("\nEnter usernames (comma-separated):")
        usernames_input = input("> ").strip()
        
        if not usernames_input:
            print("❌ No usernames provided!")
            sys.exit(1)
        
        usernames = [u.strip() for u in usernames_input.split(',') if u.strip()]
        
        print(f"\n🔍 Checking {len(usernames)} usernames...")
        print("-" * 50)
        
        results = checker.check_bulk(usernames)
        print_results_summary(results)
    
    elif choice == "3":
        # Check from file
        filename = input("\nEnter filename (one username per line): ").strip()
        
        try:
            with open(filename, 'r') as f:
                usernames = [line.strip() for line in f if line.strip()]
            
            if not usernames:
                print("❌ No usernames found in file!")
                sys.exit(1)
            
            print(f"\n🔍 Checking {len(usernames)} usernames from file...")
            print("-" * 50)
            
            results = checker.check_bulk(usernames)
            print_results_summary(results)
            
            # Save results
            save = input("\nSave results to file? (y/n): ").lower()
            if save == 'y':
                output_file = f"roblox_results_{int(time.time())}.txt"
                with open(output_file, 'w') as f:
                    f.write("ROBLOX USERNAME CHECK RESULTS\n")
                    f.write("="*50 + "\n\n")
                    
                    f.write(f"Available ({len(results['available'])}):\n")
                    for username in results['available']:
                        f.write(f"  ✅ {username}\n")
                    
                    f.write(f"\nTaken ({len(results['taken'])}):\n")
                    for item in results['taken']:
                        f.write(f"  ❌ {item['username']} (ID: {item['data']['id']})\n")
                    
                    f.write(f"\nInvalid ({len(results['invalid'])}):\n")
                    for item in results['invalid']:
                        f.write(f"  ⚠️  {item['username']}: {item['reason']}\n")
                
                print(f"✅ Results saved to: {output_file}")
        
        except FileNotFoundError:
            print(f"❌ File not found: {filename}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            sys.exit(1)
    
    else:
        print("❌ Invalid choice!")
        sys.exit(1)
    
    print("\n" + "="*50)
    print("✅ Check complete!")
    print("="*50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
