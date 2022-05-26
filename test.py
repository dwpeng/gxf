
import os
from unittest import TestCase, main

from src.gxf import GXF
from src.gxf.util import split_by_double_dash

REGISTER = '__register'
test_file = 'test/test.gff'


class TestHandle(TestCase):

    def _test_split(self, k, ks, count=-1):
        split_k1 = split_by_double_dash(k)
        if count != -1:
            ks = ks[:count]
            split_k1 = split_k1[:count]
        self.assertEqual(split_k1, ks)

    def test_split(self):
        _ = self._test_split
        _('type', ('type', 'eq', None, None))
        _('start__lt', ('start', 'lt', None, None))
        _('start__before_lower', ('start', 'eq', 'before', 'lower'), 3)
        _('type__ne__after_lower', ('type', 'ne', 'after', 'lower'), 3)

    def _test_split_handle(self, k, s1, s2):
        _, _, _, handle = split_by_double_dash(k)
        self.assertEqual(handle(s1), s2)

    def test_split_handle(self):
        _ = self._test_split_handle
        _('start__before_lower', 'S', 's')
        _('start__before_upper', 's', 'S')
        _('start__re__before_lower', 'S', 's')
        _('start__after_lower', 'S', 's')

    def _test_split_when(self, k, when):
        _, _, split_when, _ = split_by_double_dash(k)
        self.assertEqual(split_when, when)

    def test_split_when(self):
        _ = self._test_split_when
        _('start__before_lower', 'before')
        _('start__after_lower', 'after')
        _('start', None)
        _('type__re', None)
        _('type__lt', None)


class TestQuery(TestCase):

    def test_query(self):
        gxf = GXF(test_file)
        result1 = gxf.filter(type='gene')
        self.assertEqual(len(result1), 1)

        result2 = gxf.filter(start__lt=0)
        self.assertEqual(len(result2), 0)

        result3 = gxf.filter(type__re='^g')
        self.assertEqual(len(result3), 1)

        result4 = gxf.filter(type__before_upper='GENE')
        self.assertEqual(len(result4), 1)

        result5 = gxf.filter(
            type__ne='gene', start__gt=500, type='CDS', phase='0')
        self.assertEqual(len(result5), 2)

    def test_in(self):
        gxf = GXF(test_file)

        r1 = gxf.filter(type__in=['gene'])
        self.assertEqual(len(r1), 1)

        r2 = gxf.filter(phase__in=['0', '1'])
        self.assertEqual(len(r2), 5)

        r3 = gxf.filter(type__in=['CDS', 'exon'], phase__in=['0', '.'])
        self.assertEqual(len(r3), 10)

    def test_query_query(self):
        gxf = GXF(test_file)
        result = gxf.filter(type__ne='gene').filter(
            start__gt=500).filter(type='CDS').filter(phase='0')
        self.assertEqual(len(result), 2)


class TestSave(TestCase):

    gfffile = 'test/gfffile.gff3'
    gtffile = 'test/gtffile.gtf'

    def _clean_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)

    def test_to_gff(self):
        gxf = GXF(test_file)
        gxf.to_gff3(self.gfffile)
        new_gxf = GXF(self.gfffile)
        self.assertEqual(len(gxf), len(new_gxf))
        self._clean_file(self.gfffile)

    def test_to_gtf(self):
        gxf = GXF(test_file)
        gxf.to_gtf(self.gtffile)
        new_gxf = GXF(self.gtffile)
        self.assertEqual(len(gxf), len(new_gxf))
        self._clean_file(self.gtffile)


if __name__ == '__main__':
    main()
