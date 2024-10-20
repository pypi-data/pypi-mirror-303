from plutonkit.helper.template import convert_template
import unittest

RAW_TEMPLATE_NONE = """
({ 
    @none{
    ./tests/raw/tpl/test_temp.tplpy
    }
})
"""
RAW_TEMPLATE1 = """
({ 
    @content{

    from decouple import config
    from sqlalchemy import create_engine
     from sqlalchemy.orm import declarative_base,sessionmaker
    from urllib.parse import quote_plus
    }
})
{$See}
"""

RAW_TEMPLATE2 = """
({ 
    @load{
    ./tests/raw/tpl/test_temp.tplpy
    }
})
"""

RAW_TEMPLATE2_TEXT = """
({ 
    @load{
    ./tests/raw/text/empty.txt
    }
})
"""
class TestTemplate(unittest.TestCase):
    def test_convert_template_valid(self):
        TEST_RAW = """

from decouple import config
from sqlalchemy import create_engine
 from sqlalchemy.orm import declarative_base,sessionmaker
from urllib.parse import quote_plus
1
"""     

        self.assertEqual(convert_template(RAW_TEMPLATE1,{"See":"1"}), TEST_RAW)

    def test_convert_load_valid(self):
        TEST_RAW = """
if __name__ == "__main__":
    main()

"""
        self.assertEqual(convert_template(RAW_TEMPLATE2,{}), TEST_RAW)

    def test_convert_load_in_text_valid(self):
        TEST_RAW = """

"""
        self.assertEqual(convert_template(RAW_TEMPLATE2_TEXT,{}), TEST_RAW)

    def test_invalid_text(self):
        TEST_RAW = """

"""
        self.assertEqual(convert_template(RAW_TEMPLATE_NONE,{}), TEST_RAW)
