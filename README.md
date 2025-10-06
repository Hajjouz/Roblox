# Roblox Username Checker


## Features

✅ **Single Username Check** - Check if a specific username is available  
✅ **Bulk Username Check** - Check multiple usernames at once  
✅ **File Import** - Load usernames from a text file  
✅ **Real-time Validation** - Uses official Roblox API  
✅ **Detailed Results** - Shows if username is available, taken, or invalid  
✅ **Export Results** - Save results to a text file  
✅ **Rate Limiting** - Built-in delays to prevent API throttling  

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. **Clone or download the repository**

```bash
gitclone https://github.com/Hajjouz/Roblox
```

2. **Install required dependencies**

```bash
pip install requests
```

Or if you have a requirements file:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Script

```bash
python3 roblox.py
```

### Mode 1: Check Single Username

Check if a specific username is available on Roblox.

**Example:**
```
Select mode (1-3): 1
Enter username to check: CoolPlayer123

🔍 Checking username: CoolPlayer123
--------------------------------------------------

✅ USERNAME AVAILABLE!
This username can be registered on Roblox
```

### Mode 2: Bulk Check (Multiple Usernames)

Check multiple usernames at once by entering them separated by commas.

**Example:**
```
Select mode (1-3): 2
Enter usernames (comma-separated):
> CoolPlayer123, EpicGamer456, ProBuilder789

🔍 Checking 3 usernames...
--------------------------------------------------

[1/3] Checking: CoolPlayer123
  ✅ Available!

[2/3] Checking: EpicGamer456
  ❌ Taken - User ID: 123456789

[3/3] Checking: ProBuilder789
  ⚠️  Invalid - Username contains inappropriate content
```

### Mode 3: Check from File

Load usernames from a text file (one username per line).

**Example:**

1. Create a text file `usernames.txt`:
```
CoolPlayer123
EpicGamer456
ProBuilder789
AwesomeUser001
SuperHero999
```

2. Run the checker:
```
Select mode (1-3): 3
Enter filename (one username per line): usernames.txt

🔍 Checking 5 usernames from file...
--------------------------------------------------
[1/5] Checking: CoolPlayer123
  ✅ Available!
...

Save results to file? (y/n): y
✅ Results saved to: roblox_results_1728234567.txt
```

## Understanding Results

### ✅ Available
The username is valid and can be registered on Roblox.

### ❌ Taken
The username already exists on Roblox. The tool will show the User ID of the account.

### ⚠️ Invalid
The username doesn't meet Roblox requirements. Common reasons:
- Too short (minimum 3 characters)
- Too long (maximum 20 characters)
- Contains inappropriate words
- Contains special characters (only letters, numbers, and underscore allowed)
- Starts or ends with underscore
- Contains multiple consecutive underscores

## Roblox Username Rules

Valid Roblox usernames must:
- Be 3-20 characters long
- Contain only alphanumeric characters and underscores
- Not start or end with an underscore
- Not contain consecutive underscores
- Not contain inappropriate or banned words

## API Endpoints Used

This tool uses the following Roblox API endpoints:
- `https://auth.roblox.com/v1/usernames/validate` - Validate username availability
- `https://api.roblox.com/users/get-by-username` - Check if username exists

## Rate Limiting

The tool includes built-in rate limiting (0.5 seconds delay between requests by default) to avoid being throttled by Roblox API. When checking large lists, expect approximately:
- ~2 usernames per second
- ~100 usernames per minute

## Output File Format

When saving results to a file, the output format is:

```
ROBLOX USERNAME CHECK RESULTS
==================================================

Available (2):
  ✅ CoolPlayer123
  ✅ AwesomeUser001

Taken (1):
  ❌ EpicGamer456 (ID: 123456789)

Invalid (1):
  ⚠️  BadUser!!!: Username contains special characters
```

## Troubleshooting

### Connection Errors
```
Network error: Connection refused
```
**Solution:** Check your internet connection or try again later.

### Timeout Errors
```
Request timeout - please try again
```
**Solution:** Roblox API might be slow. Try reducing the number of usernames or increase the delay.

### API Rate Limiting
```
API error: 429
```
**Solution:** You're making too many requests. The tool has built-in delays, but if you encounter this, wait a few minutes before trying again.

## Advanced Usage

### Custom Delay Between Requests

If you need to modify the delay between requests, edit the script:

```python
results = checker.check_bulk(usernames, delay=1.0)  # 1 second delay
```

### Use as Python Module

You can also import and use the checker in your own Python scripts:

```python
from roblox_username_checker import RobloxUsernameChecker

checker = RobloxUsernameChecker()

# Check single username
is_valid, message = checker.validate_username("CoolPlayer123")
print(f"Valid: {is_valid}, Message: {message}")

# Check if exists
exists, user_data = checker.check_username_exists("EpicGamer456")
if exists:
    print(f"User ID: {user_data['id']}")
```

## Example Scenarios

### Scenario 1: Finding Available OG Names
Check a list of classic/OG usernames to find available ones:
```
Create file: og_names.txt
Legend
Hero
Champion
Master
King
...
```

### Scenario 2: Username Variations
Check variations of your desired username:
```
MyName
MyName123
MyName_YT
xMyNamex
MyName2024
```

### Scenario 3: Brand Protection
Check if your brand name or variations are available:
```
BrandName
BrandNameOfficial
BrandName_Official
TheBrandName
```

## Legal & Ethical Use

⚠️ **Important Notes:**
- This tool is for **legitimate username checking only**
- Do not use for username sniping or harassment
- Respect Roblox Terms of Service
- Do not abuse the API with excessive requests
- Use responsibly and ethically

## Limitations

- Requires active internet connection
- Subject to Roblox API availability and rate limits
- Cannot reserve or register usernames (checking only)
- API responses may vary based on Roblox updates

## Contributing

Feel free to submit issues or pull requests for improvements:
- Bug fixes
- New features
- Documentation improvements
- Performance optimizations

## License

This tool is provided as-is for educational and legitimate username checking purposes.

## Support

If you encounter issues:
1. Check your internet connection
2. Ensure Python 3.6+ is installed
3. Verify `requests` library is installed
4. Check if Roblox API is accessible from your location

## Changelog

### Version 1.0.0
- Initial release
- Single username check
- Bulk username check
- File import support
- Results export feature
- Rate limiting protection

---

**Created for educational purposes. Use responsibly!** 🎮
