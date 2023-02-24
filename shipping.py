weight = 41.5
# Ground Shipping & Drone Shipping
if weight <= 2:
  price_ground_shipping = weight * 1.5 + 20
  price_drone_shipping  = weight * 4.5
elif weight <= 6:
  price_ground_shipping  = weight * 3 + 20
  price_drone_shipping  = weight * 9
elif weight <= 10:
  price_ground_shipping  = weight * 4 + 20
  price_drone_shipping = weight * 12
else:
  price_ground_shipping  = weight * 4.75 + 20
  price_drone_shipping = weight * 14.75
# Price Ground Shipping Premium
price_ground_shipping_premium = 125            

if price_ground_shipping <= price_ground_shipping_premium and price_ground_shipping <= price_drone_shipping:
  print("The price for the ground shipping is: " + str(price_ground_shipping) + "€")
elif price_ground_shipping_premium <= price_drone_shipping:
  print("The price for the premium shipping is: " + str(price_ground_shipping_premium) + "€")
else:
  print("The price for the drone shipping is: " + str(price_drone_shipping) + "€")
