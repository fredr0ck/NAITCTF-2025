# Write-up: Страшен ли XOR реверсеру?

## Анализ файла
Получаем файл `crackmestrong.exe`. Анализ с помощью **IDA Pro** и других инструментов показывает, что файл написан на **C++**. В коде заметно использование функции `IsDebuggerPresent`, что говорит о попытке защиты от отладки.

## Обход защиты от отладки
Для обхода защиты от отладки используем **x64dbg** с плагином **TitanEngine**. Этот инструмент позволяет скрыть наличие отладчика и продолжить выполнение программы, минуя защиту.

## Поиск ключевых строк
Ищем строку `"Good! Flag:"`, которая появляется в коде программы и является индикатором успешного получения флага. Находим её с помощью поиска в **IDA Pro**.

## Установка BreakPoint
Ставим **breakpoint** на вызов функции:
```assembly
call crackmestrong.7FF684A211D1
```
Это позволяет остановить выполнение программы в нужной точке, чтобы далее проанализировать её поведение и найти флаг.

##Ввод флага
После остановки программы на breakpoint, вводим случайный флаг в консоль. Программа обрабатывает введённый флаг, и в FPU (Floating Point Unit) появляется важная информация.

##Получение флага
После выполнения всех шагов, программа выводит заветный флаг:

```
NAITCTF{STR0NG_Y3A?}
```