#this file is written not to use in the code but just to 
#explain the database schema 
portfolioEntity={
    "ticker":str,
    "quantity":int,
}
order={
    "ticker": str,
    "atPrice": float,
    "change":int
}
trade={
    "date": str,
    "orders":[
        order   
    ]
}

money={
        "allotedFunds":int,
        "currency":str,
    }
# in user collection
usersSchema={
    "username":str,
    "name": str,
    "password": str,
    "email":str,
    #"role": str,
    "netProfits":[money],
    "funds":[money],  
}
# in portfolioSchema
portfolioSchema={
    "_id": str,
    "portfolio":
        [
        portfolioEntity
    ],
    "trades":
        [
            trade
        ]
}
