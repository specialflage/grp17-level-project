shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
print(shopping_cart_dict)
for item in shopping_cart_dict:
    shopping_cart_dict[item] = shopping_cart_dict[item] * 1.1 #*= 1.1
print(shopping_cart_dict)

total_values_after_raise = sum (shopping_cart_dict.values())
print("\nTotal Value After 10% Price Increase:", total_values_after_raise)

vat_rate = .14

total_with_vat = total_values_after_raise * (1 + vat_rate)
total_with_vat = round(total_with_vat, 2)

print("\nTotal Value with VAT (14%):", total_with_vat)