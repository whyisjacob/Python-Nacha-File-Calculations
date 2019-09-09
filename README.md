
# Python Nacha File Editor

##### By Jacob Hershberger | Version 1.1

  

## Project Description

Working in the finance industry, you may need to manually manipulate a bank NACHA file. I have written this script to enable you to do that. Currently in the early stage of its life, this script will only recalculate a bank nacha file with credits and debits after it has been created or manipulated.

  

## Usage

 1. Make sure you have a working version of Python installed on your machine.
 2. Clone this repository down to where you typically work on your machine
 3. Create a `.txt` file with the name `"OldNacha.txt"`.
 4. Run the command `$ python recalculateNacha.py` 
 5. A new file will generate `"NEWNacha.txt"`.

## Future Planned Updates
*in no particular order*
 - Enable you to remove line items as desired from the script.
 - Enable you to run via an executable instead of being forced to have python installed on your machine.
 - other features as desired.

## License 
MIT License

Copyright (c) 2019 Jake Hershberger

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANT ABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


### Changelog
 - 1.1 added routing number recalculation clause on the batch trailer. removed unneeded comments
 - 1.0 Initial Release 