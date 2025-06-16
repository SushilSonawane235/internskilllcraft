import re

def check_password_strength(password):
    print("\n🔍 Let's take a look at your password...")

    too_short = len(password) < 8
    missing_upper = re.search(r"[A-Z]", password) is None
    missing_lower = re.search(r"[a-z]", password) is None
    missing_number = re.search(r"\d", password) is None
    missing_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Strength score
    score = 5 - sum([too_short, missing_upper, missing_lower, missing_number, missing_special])

    # Feedback
    print(f"\n📏 Length (at least 8 characters): {'✅ Great!' if not too_short else '❌ Too short!'}")
    print(f"🔠 Contains UPPERCASE letter: {'✅ Yep!' if not missing_upper else '❌ Nope.'}")
    print(f"🔡 Contains lowercase letter: {'✅ Good!' if not missing_lower else '❌ Missing.'}")
    print(f"🔢 Contains a number: {'✅ Present!' if not missing_number else '❌ Missing digits.'}")
    print(f"🔣 Contains special character (!@#$...): {'✅ Nice!' if not missing_special else '❌ None found.'}")

    # Strength rating
    print("\n🧠 Final Verdict:")
    if score == 5:
        print("🌟 Your password is **Very Strong** — good job!")
    elif score == 4:
        print("👍 That's a **Strong** password — just a little more to make it perfect.")
    elif score == 3:
        print("🟡 It's **Okay**, but could use some improvements.")
    else:
        print("🔴 This password is **Weak** — consider making it longer and adding more variety!")

def main():
    print("👋 Welcome to your friendly Password Strength Checker!")
    print("Let’s see how strong your password really is.\n")

    password = input("🔑 Enter your password: ").strip()

    if not password:
        print("⚠️ Oops! You didn’t type anything. Try again.")
        return

    check_password_strength(password)

if __name__ == "__main__":
    main()
