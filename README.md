# Typing Speed Automation Script

This is a Python script that uses Selenium WebDriver to automate typing on a typing test website (KeyHero). The script types a given block of text at a specific words per minute (WPM) rate of 102.

## Features
- Automates the typing of text in the KeyHero typing test.
- Types the text at a configurable speed (102 WPM by default).
- Allows you to change the text to be typed by modifying a variable.

## Requirements
- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (or any other browser's WebDriver)
- Chrome browser installed

### Installation

1. Install Python 3.x from the official website: https://www.python.org/
2. Install Selenium using pip:
    ```bash
    pip install selenium
    ```
3. Download the [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) matching your Chrome version.
4. Place the `chromedriver` in the same directory as your script or set the path in the script.

## Usage

1. Clone or download the repository.
2. Modify the `text_to_type` variable in the script to the text you want to type. By default, the script types a medical text, but you can change this to any text you prefer.

   ```python
   text_to_type = "Your custom text here"
   ```

3. Replace the `username` and `password` values in the script with your credentials to log in to the KeyHero typing website.
   ```python
   username_field.send_keys("your_username")
   password_field.send_keys("your_password")
   ```

4. Run the script:
    ```bash
    python typing_automation.py
    ```

5. The script will open the KeyHero typing test page, log in, and automatically type the provided text at the set speed (102 WPM).

### Changing the Text to Type

To change the text that is typed, simply update the `text_to_type` variable with your desired text:

```python
text_to_type = "Here is the new text you want to type."
```

Make sure to keep the text inside the quotation marks.

## Notes
- The script includes a 8-second delay for you to manually position the cursor in the typing area. You will be prompted to do so after logging in.
- Ensure that the Chrome WebDriver path is correctly set or is in the same folder as the script.
- You can adjust the typing speed by changing the `delay_per_word` calculation to match your desired WPM.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
