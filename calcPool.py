from math import sqrt

def calcPoolV3(lower_bound,
               upper_bound,
               tokenA_in_pool,
               tokenB_in_pool,
               current_price,
               future_price):
    """
    This function calculate the number of each tokens in a your uniswap liquidity v3 pool as
    the price(exchange ratio) varies. 
    
    Example usage: 
        Lets say your usdt/eth pool looks as follows:
            pool price range: 3000 - 5000 (usdt per eth)
            currently you have:
                500 eth and 600000 usdt in the pool
            the current price is 3400 usdt per eth
        You want to know what your pool would look like when the price is 3600 usdt per eth.
        You can call the function as shown below to find the future pool composition. 
        print(calcPoolV3(lower_bound=3000, 
                 upper_bound=5000,
                 tokenA_in_pool=500,
                 tokenB_in_pool=600000,
                 current_price=3440,
                 future_price=3600))
    
    Reference: 
        Formula provided by this website.
        https://atiselsts.github.io/pdfs/uniswap-v3-liquidity-math.pdf?utm_source=chatgpt.com
    """
    
    # Note price and bounds is the price of A in terms of B.
    if future_price > upper_bound:
        future_price = upper_bound
    if future_price < lower_bound:
        future_price = lower_bound
    
    L_A = tokenA_in_pool * (sqrt(current_price*upper_bound))/(sqrt(upper_bound)-sqrt(current_price))
    L_B = tokenB_in_pool / (sqrt(current_price)-sqrt(lower_bound))
    L = min(L_A, L_B)
    tokenA_in_pool_future = L * (sqrt(upper_bound)-sqrt(future_price))/(sqrt(future_price*upper_bound))
    tokenB_in_pool_future = L * (sqrt(future_price)-sqrt(lower_bound))
    return {
        "future A": tokenA_in_pool_future,
        "future B": tokenB_in_pool_future
    }
