import os
import falu

falu.api_key = os.environ.get('FALU_API_KEY')

balance_refresh = falu.Money.force_balance_refresh()

print("Balance Refresh Success: %r" % balance_refresh)

balances = falu.Money.get_money_balance()

print("Balances: %r" % balances.created)