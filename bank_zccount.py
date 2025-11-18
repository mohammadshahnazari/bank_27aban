accounts =  []  


n = int(input("چند حساب بانکی می‌خواهید ایجاد کنید؟ "))

for i in range(n):
    print(f"\nحساب شماره {i+1}:")
    name = input("نام صاحب حساب: ")
    balance = float(input("موجودی اولیه: "))
    accounts.append([name, balance])

while True:
    print("\n===== منوی عملیات بانکی =====")
    print("1. نمایش موجودی همه حساب‌ها")
    print("2. سپرده‌گذاری در حساب")
    print("3. برداشت از حساب")
    print("4. نمایش حساب‌هایی با موجودی بیشتر از میانگین")
    print("5. خروج")

    choice = input("انتخاب کنید: ")


    if choice == "1":
        print("\n--- لیست حساب‌ها ---")
        for acc in accounts:
            print("نام:", acc[0], "- موجودی:", acc[1])


    elif choice == "2":
        name = input("نام حساب برای سپرده‌گذاری: ")
        amount = float(input("مبلغ سپرده: "))

        found = False
        for acc in accounts:
            if acc[0] == name:
                acc[1] += amount
                print("سپرده‌گذاری انجام شد. موجودی جدید:", acc[1])
                found = True

        if not found:
            print("حسابی با این نام پیدا نشد!")


    elif choice == "3":
        name = input("نام حساب برای برداشت: ")
        amount = float(input("مبلغ برداشت: "))

        found = False
        for acc in accounts:
            if acc[0] == name:
                found = True
                if acc[1] >= amount:
                    acc[1] -= amount
                    print("برداشت انجام شد. موجودی جدید:", acc[1])
                else:
                    print("خطا: موجودی کافی نیست!")

        if not found:
            print("حسابی با این نام وجود ندارد!")


    elif choice == "4":
        total = 0
        for acc in accounts:
            total += acc[1]

        avg = total / len(accounts)
        print("\nمیانگین موجودی حساب‌ها:", avg)

        print("\n--- حساب‌های با موجودی بیشتر از میانگین ---")
        for acc in accounts:
            if acc[1] > avg:
                print("نام:", acc[0], "- موجودی:", acc[1])


    elif choice == "5":
        print("خروج از برنامه...")
        break

    else:
        print("گزینه نامعتبر! دوباره وارد کنید.")
