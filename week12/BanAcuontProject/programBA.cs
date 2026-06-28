using System;
namespace projectDay1
{
    enum ClassAcountType
    {
        Saving,
        Checking,
        Business
    }

    class BankAccount
    {
        private List<string> _transactions = new List<string>();

        private int _acountnumber;
        private string _ownername;
        private double _balance;
        private string _acounttype;
        private bool _isactive;



        public int AcountNumber
        {
            get
            {
                return _acountnumber;
            }
        }

        public string Ownername
        {
            get
            {
                return _ownername;
            }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                {
                    _ownername = "Unknow";
                }
                else
                {
                    _ownername = value;
                }


            }
        }

        public double Balance
        {
            get
            {
                return _balance;
            }
            set
            {
                if (value < 0)
                {
                    _balance = 0;
                }
                else
                    _balance = value;
            }
        }
        public string AcountType
        {
            get
            {
                return _acounttype;
            }
            set
            {
                if (Enum.TryParse<ClassAcountType>(value,true, out ClassAcountType type))
                    {
                        _acounttype = type.ToString();
                    }
                else
                {
                    _acounttype = ClassAcountType.Saving.ToString();
                }
            }
        }
        public bool IsActive
        {
            get
            {
                return _isactive;
            }
            private set
            {
                _isactive = value;
            }
        }
        public BankAccount(int acountNumber, string ownerName, double balance, string accountType)
        {
            _acountnumber = acountNumber;
            Ownername= ownerName;
            Balance = balance;
            AcountType= accountType;
            IsActive = true;
        }
        public BankAccount(int AcountNumber, string ownerName) : this (AcountNumber, ownerName, 0.0, "Checking")
        { 
        }
        public override string ToString()
        {
            return $"Account #{_acountnumber} | Owner: {_ownername} | Balance: ${_balance:F2} | Type: {_acounttype}";
        }
        public void Deposit(double amount)
        {
            if (0 <  amount)
            {
                Balance += amount;
                Console.WriteLine("add to balance");
                _transactions.Add($"Deposited ${amount:F2}");
            }
            else
            {
                Console.WriteLine("amount not a valibal");
            }
        }
        public bool Withdraw(double amount)
        {
            if (_balance > amount)
            {
                Balance -= amount;
                _transactions.Add($"Withdrew ${amount:F2}");
                Console.WriteLine("Withdraw with balance");
                return true;
            }
            Console.WriteLine("you no have money");
            return false;
        }
        public void ApplyInterest()
        {
            if(AcountType == "Saving")
            {
                Balance += (_balance / 100 * 2);
            }
        }
        public void PrintTransactionHistory()
        {
            foreach (string transaction in _transactions)
            {
                Console.WriteLine(transaction);
            }
        }

        public void Activate()
        {
            IsActive = true;
        }

        public void Deactivate()
        {
            IsActive = false;
        }

        public static bool Transfer(BankAccount from, BankAccount to, double amount)
        {
            if (!from.IsActive || !to.IsActive)
            {
                Console.WriteLine("account noy active");
                return false;
            }

            if (amount <= 0)
            {
                Console.WriteLine("Amount not valibal");
                return false;
            }

            if (from.Balance < amount)
            {
                Console.WriteLine("no have money");
                return false;
            }

            from.Withdraw(amount);
            to.Deposit(amount);

            return true;
        }
    }
    class Program
    {
        static void Main()
        {
            List<BankAccount> accounts = new List<BankAccount>();

            accounts.Add(new BankAccount(1, "Meir", 1000, "Checking"));
            accounts.Add(new BankAccount(2, "David", 2500, "Saving")); 
            accounts.Add(new BankAccount(3, "Avi", 5000, "Business")); 
            accounts.Add(new BankAccount(4, "Moshe"));                   
            accounts.Add(new BankAccount(5, "arial"));
            accounts.Add(new BankAccount(6, "", 1000, "Checking"));

            foreach (BankAccount account in accounts)
            {
                Console.WriteLine(account);
            }
            accounts[0].Deposit(300);
            accounts[2].Withdraw(100);
            accounts[2].Withdraw(10000);

            accounts[0].Deactivate();
            Console.WriteLine(accounts[0].IsActive);



            foreach (BankAccount account in accounts)
            {
                account.ApplyInterest();
            }

            Console.WriteLine("result:");

            foreach (BankAccount account in accounts)
            {
                Console.WriteLine(account);
            }
        }
    }
}
