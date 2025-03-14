class Program
{
    static void Main()
    {
        string flag = "NAITCTF{1ts_N41T_4ND_M3}";
        Console.Write("Enter the flag: ");
        string input = Console.ReadLine();

        if (flag == input)
        {
            Console.WriteLine("Correct flag!");
            Console.ReadKey();
        }
        else
        {
            Console.WriteLine("Wrong flag!");
            Console.ReadKey();
        }
    }
}
