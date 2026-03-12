from wallet_package.data import *
from wallet_package.auth import *
from wallet_package.profile import *
from wallet_package.log import *
from datetime import datetime
from wallet_package.exceptions import *

class Wallet:

    calculate_fee = staticmethod(lambda amount, fee_rate: amount * fee_rate)


    def get_limit(self):
        return self.user.get_transaction_limit()

    def __init__(self,User,Auth):
        self.user = User
        self.auth = Auth
        self.user_transactions = []

    

   

    def debit_penalty(self):
        
        try:
            if(self.user.wallet_balance < self.auth.MINIMUM_BALANCE):
                penalty = 50
                self.user.wallet_balance -= penalty
                print(" the wallet balance after penalty", self.user.wallet_balance)
            else:
                print(" No penalty- Balance:",self.user.wallet_balance)
        except TypeError as e:
            print(f"TypeError Caught: {e}")
        except Exception as e:
            print(f"UnKnown Error Caught: {e}")
        finally:
            print("the debit_penalty function is attempted here")
    # debit_penalty(50)

    def add_interst(self, rate):
        
        print("Before intrest:", self.user.wallet_balance)
        try:
            if self.user.is_active and self.user.wallet_balance > self.auth.MINIMUM_BALANCE:
                
                intrest_amt = self.user.wallet_balance*rate
                self.user.wallet_balance +=intrest_amt
                print(" intrest amount:",intrest_amt)
                print("final balance:",self.user.wallet_balance)
            else:
                print("Cannot add intrest, check the balance")
        except TypeError as e:
            print(f"TypeError Caught: {e}")
        except Exception as e:
            print(f"UnKnown Error Caught: {e}")
        finally:
            print("the add_interst function is attempted here")
    

    

    def check_validity(func):
        def validate(self,args,kwargs="credit"):
            try:
                if self.auth.validate_transaction(self.user.wallet_balance, self.user.is_active) and self.auth.check_user_transaction():
                    return func(self,args,kwargs)
                else:
                    print("auth is failed")
            except Exception as e:
                print(f"UnKnown Error Caught: {e}")
        return validate
        

    @check_validity
    def add_transaction(self,new_transaction, type="credit"):
        
        print("-------------------\n")
        try:
            fee = self.calculate_fee(new_transaction, self.user.get_fee_rate())
            
            if new_transaction < self.get_limit():
                if type == "debit":
                    total_amount = new_transaction +fee
                    total_amount = - total_amount
                else:
                    total_amount = new_transaction - fee
                print("the initial balance: ",self.user.wallet_balance)
                self.user_transactions.append((total_amount, datetime.now() ))
                self.user.wallet_balance += total_amount
                print("updated balance: ", self.user.wallet_balance)
                print(f"the transaction fee is {fee}")
                print("the updated user transactions list: ",self.user_transactions)
                # print("The user transactions array",user_transactions_array)

                Logger.log_transaction(action=f"{type} Transaction", amount=total_amount)
            else:
                print(f"user inactive or limit reached: {self.get_limit()}")
                Logger.log_transaction(action="Transaction failed",amount=new_transaction )

        except TypeError as e:
            print(f"TypeError Caught: {e}")
            Logger.log_transaction(action="Type error occured, check the amount given", amount=new_transaction)
        except ValueError as e:
            print(f"ValueError Caught: {e}")
            Logger.log_transaction(action="Value error occured, check the amount given", amount=new_transaction)
        except Exception as e:
            print(f"UnKnown Error Caught: {e}")
            Logger.log_transaction(action="UnKonwn error occured", amount=new_transaction)
        finally:
            print("the add_transaction function is attempted here")
    # add_transaction(300.0)

    def account_history(self):
        try:
            if not self.user_transactions:
                print("No transactions found")
                return
            for amount, timestamp in self.user_transactions:
                print(f"Amount: {amount}, Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print("Error Caught:",e)



    # def transaction_generator():
    #     global user_transactions
    #     try:
    #         if not user_transactions:
    #             raise ValueError("no transactions found")
    #         for index, transaction in enumerate(user_transactions):
    #             message = yield transaction
    #             if message:
    #                 print(f"message recieved: {message}")
    #     except ValueError as e:
    #         print(f"ValueError Caught: {e}")
    #     except Exception as e:
    #         print(f"UnKnown Error Caught: {e}")
    #     finally:
    #         print("the transaction_generator function is attempted here")
    # # gen = transaction_generator()
    # # print(f"listof trans : {list(gen)}")
    # # print(f"first : {next(gen)}")
    # # print(gen.send("this is the message"))
    # # print(f"second: {next(gen)}")


class PremiumWallet(Wallet):
    def get_fee(self, amount):
        return self.calculate_fee(amount, self.user.get_fee_rate())
    
    def add_transaction(self, new_transaction, type="credit"): # overridden
        new_transaction = float(new_transaction)
        super().add_transaction(new_transaction, type)
        if self.user.account_type == "Premium":
            self.user.add_cashback(new_transaction)

    def add_interst(self, rate):
        if self.user.account_type == "Premium":
            rate += 0.01
        super().add_interst(rate)

    def debit_penalty(self):
        if self.user.account_type == "Premium":
            penalty = 25
            self.user.wallet_balance -= penalty
            print(f"Penalty of {penalty}, new balance is : {self.user.wallet_balance}")
        else:
            super().debit_penalty()