# Write-up: Обфускация кода

## Анализ файла
Получаем файл `Task5Amazing.exe` и, используя анализаторы, видим, что он обфусцирован. Для дальнейшего анализа открываем файл в **DnSpy**, чтобы разобраться в логике программы.

## Открытие кода
Открываем класс **Form1.cs**, где находим обработчик события `guna2Button1_Click` с таким кодом:

```csharp
private void guna2Button1_Click(object sender, EventArgs e)
{
    string b = <Module>.VaultVM_Protect_H9BC19H92a(<Module>.VaultVM-Protect-7FCFC7658C, <Module>.VaultVM-Protect-C1G49F7G7L);
    bool flag = this.sdapwdlsdx.Text == b;
    if (flag)
    {
        MessageBox.Show(<Module>.VaultVM_Protect_H9BC19H92a(<Module>.VaultVM-Protect-9ABA13F4G3, <Module>.VaultVM-Protect-LCF6B0A6D1));
    }
    else
    {
        MessageBox.Show(<Module>.VaultVM_Protect_H9BC19H92a(<Module>.VaultVM-Protect-HH25A00BH9, <Module>.VaultVM-Protect-91GDAEFA8A));
    }
}
```
Здесь мы видим, что программа сравнивает текст из текстового поля sdapwdlsdx с результатом выполнения метода <Module>.VaultVM_Protect_H9BC19H92a с двумя аргументами. Если строки совпадают, программа выводит сообщение о успешности, в противном случае — сообщение об ошибке.

##Установка BreakPoint
Для того чтобы узнать, что именно происходит при проверке, ставим breakpoint на условие if (flag). Это позволит нам увидеть, что происходит, когда строка из текстового поля совпадает с результатом вычисления.

##Ввод флага
После установки точки останова, запускаем программу и вводим случайный текст в текстовое поле. Когда программа достигнет точки останова, мы сможем исследовать содержимое переменных и понять, как должен выглядеть правильный флаг.

##Получение флага
После успешной проверки флага в локальных переменных появляется следующий текст:

```
NAITCTF{Br3ak_P0int_G00d!}
```