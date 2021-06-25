# KZVG: Заполнятор договоров 3000

Заполняет шаблон договора в .docx данными из формы. Помогает не множить сущности и не искать по коллегам "последний использованный договор, чтобы скопировать туда данные нового клиента": правильный шаблон всегда ведется в одном месте, а контракты только происходят от него, наследуя общие признаки.

Собрано на коленке для нужд юридической фирмы [Казарновски Групп](https://kzvg.ru), в которой я руковожу таможенной практикой. Пока что работает только под Microsoft Windows.

Архивы с бинарниками - [в разделе Releases](httphttps://github.com/medotkato/docbuilder/releases). Скачиваем, распаковываем, читаем README. Запускаем и работаем.

## Порядок использования:

1. Размечаешь .docx шаблон в /in/template_contract.docx, вставляя в него плейсхолдеры вида {{ some_placeholder1 }} ... {{ some_placeholder2 }} там, где надо заполнять данными из формы
2. Создаешь конфиг для формы в /in/form_config.yaml, в котором указывашь заголовок формы, лого и поля для заполнения (some_placeholder1, some_placeholder2, etc.) - это yaml, там все просто и очевидно.
3. Запускаешь форму

    ``` bash
    python formbuilder.py -c "in\yaml_config.yaml"
    ```

    Ну или просто

    ``` bash
    test\formbuilder.cmd
    ```

4. Заполняешь поля формы, как надо, и жмешь "Заполнить договор"
5. Забираешь заполненный договор в папке /out/docx с именем вида YYMMDD-HHMMSS_Contract_Filled.docx
6. ???
7. PROFIT!

## ETC

- История разработки: [Changelog.md](CHANGELOG.md)
- Что еще нужно (хотелось бы) сделать: [TODO.md](TODO.md)
- Лицензия: Копилефт, GPL v3 и CC BY-SA 4.0. См. [License.md](LICENCE.md)
