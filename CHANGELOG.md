# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

-

## [0.55] - 2021-06-24

- протестировал упаковку в бинарник с помощью pyinstall
- оформил requirements.txt для быстрого развертывания нужной для исполнения среды с pip:

  ```
  pip install -r requirements.txt
  ```

## [0.5] - 2021-06-23

### Added

- заполнение docx документа происходит по нажатию кнопке "Заполнить договор"
- все собрано воедино и протестировано

### Changed

- шаблоны документа и формы теперь лежат в /in
- выходные документы складываются в /out/data_yaml (сырые данные) и /out/docx (документ Word)
- документ и форма собираются из конфига в кодировке UTF-8, а не CP-1251


## [0.2] - 2021-06-22

### Added

- readme.md с ответами на вопросы "зачем" и "как"
- метки полей в yaml с данными документа
- отображение формы wx на основе конфига/шаблона в .yaml (formbuilder.py)
- файлы лицензий и changelog
- formbuilder для создания формы заполнения договора
- тестовые скрипты для запуска докбилдера и формы
- Some_Contract_Template.docx с открытым шаблоном контракта KZVG, но без некоторых чувствительных деталей
- аргументы в docbuilder и frombuilder для CLI

### Changed

- создание документа из .docx шаблона теперь из конфига в .yaml, а не json (docbuilder.py)
- раздение кода docbuiler на yaml_handler и docbuilder

## [0.1] - 2021-05-05

- docbuilder.py, который заполняет .docx шаблон с плейсхолдерами данными из json-конфига
