class BankAccount
{
    private int _accountNumber { get; }
    public int AccountNumber { get => _accountNumber; }

    private string _ownerName { get; set; }
    public string OwnerName
    {
        get => _ownerName;
        set
        { if (string.IsNullOrWhiteSpace(value)) { _ownerName = "Unknown"; }
          else { _ownerName = value; } }
    }

    private double _balance { get; set; }
    public double Balance
    {
        get => _balance;
        set
        { if (value < 0) { _balance  = 0; }
        else { _balance = value; } }
    }

    private string _accountType { get; set; }
    public string AccountType
    {
        
        get => _accountType;
        set
        {if (string.IsNullOrWhiteSpace(value)){_accountType = "Checking";return;}
        string normal = char.ToUpper(value[0]) + value.Substring(1).ToLower();
        if (!new[] { "Savings", "Checking", "Business" }.Contains(normal)){ _accountType = "Checking"; }
        else { _accountType = value; } }
    }

    public bool IsActive { get; private set; } = true;
    public void Activate() { IsActive = true; }
    public void Deactivate() { IsActive = false; }

    List<string> _transactionHistory = new List<string>();
    
    public BankAccount(int accountNumber, string ownerName, double balance, string accountType)
    {
        _accountNumber = accountNumber;
        OwnerName = ownerName;
        Balance = balance;
        AccountType = accountType;
    }
    public BankAccount(int accountNumber, string ownerName) : this (accountNumber, ownerName, 0.0, "Checking"){ }

    public override string ToString() 
        => $"Account #{_accountNumber} | Owner: {OwnerName} | Balance: ${Balance} | Type: {AccountType}";

    public void Deposit(double amount)
    {
        if (!IsActive) { Console.WriteLine("Deative account cannot deposit"); return; }
        if (amount <=  0) { Console.WriteLine("Must deposit more than zero"); return; }
        Balance += amount; _transactionHistory.Add($"Depositing ${amount} to account {AccountNumber}");
    }

    public bool Withdraw(double amount) 
    {
        if (!IsActive) { Console.WriteLine("Deative account cannot withdrow"); return false; }
        if (amount <= 0) { Console.WriteLine("Must Withdraw more than zero"); return false; }
        if (amount > Balance) { Console.WriteLine("Not enough credit"); return false; }
        Balance -= amount; _transactionHistory.Add($"Withdrowing ${amount} from account {AccountNumber}"); return true;
    }

    public void ApplyInterest() { if (AccountType == "Savings") { Balance *= 1.02; } }

    public void PrintTransactionHistory() { foreach (string t in _transactionHistory) { Console.WriteLine(t); } }

    public static bool Transfer(BankAccount from, BankAccount to, double amount)
    {
        if (from.Withdraw(amount)) { to.Deposit(amount); return true; }
        Console.WriteLine("Transfer failed");
        return false;
    }
}

class Accounts
{
    static void Main()
    {
        List<BankAccount> bal = new List<BankAccount>();
        bal.Add(new BankAccount(100, "", 100, "Savings"));
        bal.Add(new BankAccount(101, "Haim Somer", 100, ""));
        bal.Add(new BankAccount(102, "Yosef Havi", -100, "Checking"));
        bal.Add(new BankAccount(103, "Moshe Shalom", 100, "Business"));
        bal.Add(new BankAccount(104, "David Levi"));
        foreach (BankAccount account in bal) {Console.WriteLine(account.ToString()); }
        Console.ReadKey();
    }
}
