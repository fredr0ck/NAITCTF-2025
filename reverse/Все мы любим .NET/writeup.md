# Writeup: Все мы любим .NET

## Анализ файла

Сначала загружаем полученные файлы и анализируем их с помощью **Detect It Easy (DIE)**. Получаем следующую информацию:

- **Язык**: MSIL / C#
- **Библиотека**: .NET Core (v8.0, CLR v4.0.30319)

Эта информация говорит нам, что бинарный файл написан на C# и использует .NET Core. Следовательно, для дальнейшего реверса нам понадобится инструмент **dnSpy**.

## Декомпиляция в dnSpy

Открываем **dll**-файл в **dnSpy**, затем:

1. В проводнике **Assembly Explorer** находим загруженную библиотеку.
2. Нажимаем **ПКМ** (правой кнопкой мыши) по файлу и выбираем **"Перейти к точке входа"**.
3. Получаем следующий код:

```csharp
using System;

internal class Program
{
    private static void Main()
    {
        string a = "NAITCTF{1ts_N41T_4ND_M3}";
        Console.Write("Enter the flag: ");
        string b = Console.ReadLine();
        if (a == b)
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
```

## Извлечение флага

В строке `string a = "NAITCTF{1ts_N41T_4ND_M3}";` содержится искомый флаг:

```
NAITCTF{1ts_N41T_4ND_M3}
```

Таким образом, задача была решена простым анализом бинарника и извлечением строки с флагом через декомпилятор dnSpy.

