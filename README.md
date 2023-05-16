# Run_autotests_for_different_interface_languages
## Synopsis:

The repository contains my solution, of the task: Run autotests for different interface languages from Test Automation with Selenium and Python course on Stepik educational platform.

[The link on the task](https://stepik.org/lesson/237240/step/10?unit=209628)

Мое окружение:
My environment: Ubuntu 22.04.2 LTS, 64-bit
Chromium Version 113.0.5672.63 (Official Build) snap (64-bit)
Firefox 113.0.1 (64-bit)

При запуске Chrome браузера (установленный через snap) у меня возникала 
проблема в том что передаваемый язык не изменялся, 
конфиг файл (Preferences) с указанием языка не подхватывался.
Что бы решить проблему мне пришлось воспользоваться 
опцией '--user_data_dir'  с указанием временной папки в папке проекта.
Для запуска я использую bush скрипт (run_pytest.sh)
Вы можете попробовать запускать через run_pytest.sh. При этом менять параметры языка прямо в run_pytest.sh.
Или можете попробовать запустить с помощью команд из урока. Возможно Вашем окруженнии они сработают.
