import datetime
import random

print("--- 🛒 एडवांस्ड डिजिटल बिलिंग सिस्टम में आपका स्वागत है ---")
print("(बिलिंग बंद करने के लिए सामान के नाम में 'exit' लिखें)\n")

# 1. डेटा स्टोर करने और शुरुआती तैयारी
items_list = []
total_bill = 0

# रसीद के लिए रैंडम बिल नंबर और असली समय जेनरेट करना
invoice_no = random.randint(10000, 99999)
current_time = datetime.datetime.now().strftime("%d-%b-%Y | %I:%M %p")

# 2. अंतहीन इनपुट लूप
while True:
    item_name = input("सामान का नाम (या 'exit'): ").strip()
    
    if item_name.lower() == 'exit':
        break
        
    if not item_name:
        print("❌ सामान का नाम खाली नहीं हो सकता!\n")
        continue

    # 3. एरर हैंडलिंग (Try-Except) ताकि गलत इनपुट पर कोड क्रैश न हो
    try:
        price = float(input(f"'{item_name}' की कीमत (₹): "))
        quantity = int(input(f"'{item_name}' की मात्रा (Quantity): "))
        
        if price <= 0 or quantity <= 0:
            print("❌ कीमत और मात्रा 0 से बड़ी होनी चाहिए!\n")
            continue
            
    except ValueError:
        print("❌ अमान्य इनपुट! कृपया केवल संख्या (Numbers) ही दर्ज करें।\n")
        continue

    # गणित और लिस्ट में सेव करना
    item_total = price * quantity
    total_bill += item_total
    
    # टेबल फॉर्मेट के लिए डिक्शनरी बनाकर लिस्ट में डालना
    items_list.append({
        'name': item_name,
        'qty': quantity,
        'price': price,
        'total': item_total
    })
    print(f"✔️ {item_name} का बिल जोड़ा गया: ₹{item_total:.2f}\n")

# 4. फाइनल बिल प्रोसेसिंग (आपके बताए अनुसार माइनस और प्लस का क्रम)
original_total = total_bill
discount = 0
discount_msg = "कोई डिस्काउंट नहीं (बिल ₹1000 से कम है)"

# पहले डिस्काउंट का हिसाब (माइनस करना)
if original_total >= 3000:
    discount = 200
    discount_msg = "🎉 ₹200 का बंपर डिस्काउंट मिला!"
elif original_total >= 1000:
    discount = 50
    discount_msg = "🎉 ₹50 का स्पेशल डिस्काउंट मिला!"

# डिस्काउंट घटाने के बाद जो बिल बचा (Total Bill)
total_after_discount = original_total - discount

# बचे हुए बिल पर जीएसटी का हिसाब (18% टैक्स)
gst_amount = total_after_discount * 0.18

# अंतिम देय राशि (टैक्स को प्लस करना)
final_payable = total_after_discount + gst_amount

# 5. प्रोफेशनल रसीद प्रिंटिंग (मॉल स्टाइल)
print("\n" + "="*45)
print("             📜 **नाइम सुपरमार्ट**             ")
print(f"रसीद नं: #{invoice_no}       तारीख: {current_time}")
print("="*45)

# टेबल हेडर
print(f"{'सामान का नाम':<15} {'मात्रा':<6} {'दर (₹)':<8} {'कुल (₹)':<8}")
print("-"*45)

# लूप चलाकर टेबल रो प्रिंट करना
for item in items_list:
    print(f"{item['name']:<15} {item['qty']:<6} {item['price']:<8.2f} {item['total']:<8.2f}")

# निचला हिस्सा - माइनस और प्लस का साफ क्रम
print("-"*45)
print(f"💰 कुल वास्तविक बिल       : ₹{original_total:.2f}")
print(f"🎁 डिस्काउंट (माइनस)       : -₹{discount:.2f} ({discount_msg})")
print(f"💵 डिस्काउंट के बाद बिल    : ₹{total_after_discount:.2f}")
print(f"🧾 GST 18% (प्लस)        : +₹{gst_amount:.2f}")
print("="*45)
print(f"💥 अंतिम देय राशि (Payable) : ₹{final_payable:.2f}")
print("="*45)
print("   🌟 थैंक यू! नईम कोडिंग मास्टर सिस्टम 🌟   ")
print("="*45)
