#!/usr/bin/env python3
"""
Email Configuration Setup Script for Visiting Card Reader
Helps configure Gmail SMTP for password reset functionality
"""

import os
import sys
from pathlib import Path


def print_header(text):
    print("\n" + "=" * 80)
    print(text.center(80))
    print("=" * 80)


def print_section(text):
    print("\n" + "-" * 80)
    print(text)
    print("-" * 80)


def main():
    print_header("PASSWORD RESET EMAIL CONFIGURATION")

    print(
        """
This script will help you configure Gmail SMTP credentials for sending
password reset emails to users in both c4i4.org and indi4.io domains.

USERS IN SYSTEM:
  c4i4.org domain (5 users):
    - admin@c4i4.org (Admin)
    - ankita.sharma@c4i4.org
    - disha.rajpal@c4i4.org
    - natasha.acharya@c4i4.org
    - pranav.pankhawala@c4i4.org
  
  indi4.io domain (3 users):
    - adwait.deshpande@indi4.io
    - ahmed.bilal@indi4.io
    - kiran.tondchore@indi4.io

TOTAL: 8 users (from 2 domains)
"""
    )

    print_section("STEP 1: GET GMAIL APP PASSWORD")
    print(
        """
1. Go to https://myaccount.google.com/
2. Click "Security" in the left sidebar
3. Enable "2-Step Verification" (if not already enabled)
   - Follow the prompts to verify your identity
4. Go back to Security settings
5. Find "App passwords" (appears only if 2FA is enabled)
6. Select "Mail" and "Windows Computer"
7. Google will generate a 16-character password
8. Copy this password (it will look like: abcd efgh ijkl mnop)

KEEP THIS PASSWORD SAFE!
"""
    )

    print_section("STEP 2: UPDATE .env FILE")
    print(
        """
Open the .env file in the project root and update these lines:

BEFORE:
  SMTP_USERNAME=your_gmail@gmail.com
  SMTP_PASSWORD=your_16_char_app_password

AFTER (example):
  SMTP_USERNAME=noreply@gmail.com
  SMTP_PASSWORD=abcdefghijklmnop

Notes:
  - Remove spaces from the app password
  - Use the same email for SENDER_EMAIL
  - Keep SMTP_SERVER=smtp.gmail.com
  - Keep SMTP_PORT=587
"""
    )

    print_section("STEP 3: RESTART FLASK")
    print(
        """
After updating .env, restart Flask to load the new credentials:

  Get-Process python | Stop-Process -Force
  python back.py

Watch the Flask console for confirmation messages.
"""
    )

    print_section("STEP 4: TEST PASSWORD RESET")
    print(
        """
Test the complete password reset flow:

1. Go to: http://127.0.0.1:5000/forgot-password
2. Enter email: disha.rajpal@c4i4.org (test user from c4i4.org)
3. Check the email for reset link
4. Follow the reset link and set a new password
5. Login with the new password

OR test with indi4.io user:
1. Enter email: adwait.deshpande@indi4.io
2. Check the email for reset link
3. Reset password and login
"""
    )

    print_section("WHAT HAPPENS AFTER SETUP")
    print(
        """
Once SMTP is configured:

1. User clicks "Forgot Password"
2. Enters email address (c4i4.org or indi4.io)
3. Receives email with reset link containing secure token
4. Clicks link and creates new password
5. Logs in with new password

Email includes:
  - Professional HTML formatting
  - Company branding
  - Gradient colored reset button
  - Security notice
  - Clear instructions

Admin Protection:
  - admin@c4i4.org cannot reset password through this flow
  - Admin must be reset by system administrator
"""
    )

    print_section("SECURITY FEATURES")
    print(
        """
✓ Strong Password Requirements:
  - Minimum 8 characters
  - Uppercase letter (A-Z)
  - Lowercase letter (a-z)
  - Digit (0-9)
  - Special character (!@#$%^&*)

✓ Secure Token Generation:
  - 256-bit cryptographic entropy
  - Expires after use
  - Cannot be reused

✓ Password Storage:
  - Hashed with bcrypt
  - Salted automatically
  - Never stored in plaintext

✓ Email Validation:
  - Works for both c4i4.org and indi4.io domains
  - Prevents user enumeration
  - Case-insensitive handling
"""
    )

    print_section("TROUBLESHOOTING")
    print(
        """
Problem: "Email not sent: SMTP credentials not configured"
Solution: 
  - You haven't updated SMTP_USERNAME and SMTP_PASSWORD yet
  - Or the placeholders are still in the .env file
  - Update .env with actual Gmail credentials

Problem: "SMTP Authentication Error"
Solution:
  - Gmail credentials are incorrect
  - Make sure you're using the App Password (not account password)
  - App Password is 16 characters
  - Verify 2FA is enabled on the Gmail account

Problem: Email not received
Solution:
  - Check spam/junk folder
  - Verify SENDER_EMAIL matches the Gmail account
  - Check Flask console for error messages
  - Ensure Gmail account allows "Less secure apps" or using App Password

Problem: Reset link doesn't work
Solution:
  - Click the link immediately (tokens don't have expiry in current implementation)
  - Make sure you're clicking the full link
  - Check that Flask is still running
"""
    )

    print_section("NEXT STEPS")
    print(
        """
1. Obtain Gmail App Password from your Gmail account
2. Update SMTP_USERNAME and SMTP_PASSWORD in .env
3. Restart Flask with new credentials
4. Test password reset for both domains
5. Verify emails are received

Questions? Check the logs in Flask console for detailed error messages.
"""
    )

    print_header("READY TO CONFIGURE")
    print(
        """
Once you have your Gmail App Password:
1. Open .env file
2. Update SMTP_USERNAME and SMTP_PASSWORD
3. Save and restart Flask
4. Test the forgot password functionality
"""
    )


if __name__ == "__main__":
    main()
