file_path = r"D:\kk\New folder\Python\30 days Pyhton Challenge\Day wise\Day_10\Daily_sales.txt"

try:
    file = open(file_path, "r")
    total_sales = 0
    day = 1

    for line in file:
        try:
            sales = float(line.strip())
            print(f"✅ Day {day}: ₹{sales}")
            total_sales += sales
        except ValueError:
            print(f"⚠️ Day {day}: Invalid entry '{line.strip()}' — Skipped.")
        day += 1

    print(f"\n🧾 Total Sales: ₹{total_sales:.2f}")

except FileNotFoundError:
    print(f"\n❌ Error: Could not find the file at '{file_path}'.")

except Exception as e:
    print(f"\n⚠️ Unexpected error occurred: {e}")

finally:
    if 'file' in locals():
        file.close()
        print("📁 File closed after reading sales data.")
