def initialize(context):
    context.asset = sid(24)
    #sid (Stock ID)
   
def handle_data(context, data):
    #Data is your universe of info
    hist = data.history(context.asset, 'price', 50, '1d')
    #hist is your history(asset, field, bar_count, frequency
    #Simple moving average crossover strategy
    log.info(hist.head())
    sma_50 = hist.mean()
    sma_20 = hist[-20:].mean()
    
    open_orders = get_open_orders()
    
    if sma_20 > sma_50:
        if context.asset not in open_orders:
            order_target_percent(symbol('AAPL'), 1.0)
    elif sma_50 > sma_20:
        if context.asset not in open_orders:
            order_target_percent(symbol('AAPL'), -1.0)
        
    record(leverage = context.account.leverage)
