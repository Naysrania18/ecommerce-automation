import time

def live_demo():
    print("\n" + "="*50)
    print("       🚀 LIVE DEMO - E-COMMERCE AUTOMATION")
    print("="*50)
    
    steps = [
        ("1. User Login", "✅ Simulating login with credentials"),
        ("2. Product Search", "✅ Searching for 'laptop' products"),
        ("3. Add to Cart", "✅ Adding 3 items to shopping cart"),
        ("4. Checkout Process", "✅ Processing payment of ₹12,499"),
        ("5. Order Confirmation", "✅ Order #ORD789456 confirmed!")
    ]
    
    for step, message in steps:
        print(f"\n{step}:")
        print(f"   {message}")
        time.sleep(1)
    
    print("\n" + "="*50)
    print("       🎉 DEMO COMPLETED SUCCESSFULLY!")
    print("="*50)
    return True

if __name__ == "__main__":
    live_demo()