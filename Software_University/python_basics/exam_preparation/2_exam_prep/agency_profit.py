airline_name = input()
grownup_tickets_count = int(input())
kids_tickets_count = int(input())
net_worth_grownup_ticket_price = float(input())
service_fee = float(input())

net_worth_kids_ticket_price = net_worth_grownup_ticket_price - (net_worth_grownup_ticket_price * 0.7)
grownup_tickets_price_plus_service_fee = net_worth_grownup_ticket_price + service_fee
kids_tickets_price_plus_service_fee = net_worth_kids_ticket_price + service_fee
total_tickets_price = (kids_tickets_count * kids_tickets_price_plus_service_fee) + (grownup_tickets_count * grownup_tickets_price_plus_service_fee)
income = total_tickets_price * 0.2

print(f"The profit of your agency from {airline_name} tickets is {income:.2f} lv.")