import unittest
import os
from z_score_target_engagement import *
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)


class TestSimpleCase(unittest.TestCase):
    # These test are for the math behind median normalization and z score calculation for peptides. 
    # The "correct" answers have been independently verified in depth.

    test_path = os.path.join(os.getcwd(), "test", "simple_test_peptides.csv")

    def setUp(self):
        self.dl = DataLoader()
        self.p = PeptideProcessor(label_screens=False)
        self.data_container = self.dl.load_data(self.test_path, filetype="encyclopedia")
        self.z = PeptideZScoreCalculator()
        self.true_sum = -132.53010423036116 # what the z scores should sum to

    def test_data_load(self):
        self.assertIsInstance(self.data_container.raw_df, pd.DataFrame)

    def test_peptide_processor(self):
        self.p.process_and_normalize(self.data_container)
        quant_cols = [col for col in self.data_container.normalized_df.columns if col not in [('batch', '', ''), ('Compound', '', ''),('screen', '', '')]]
        col_medians = self.data_container.normalized_df[quant_cols].median().to_list()
        self.assertEqual(col_medians, [-2.2440416373814354, 0.0, 2.308756486898588])
    
    def test_compute_z_score(self):
        self.p.process_and_normalize(self.data_container)
        self.z.compute_z_score(self.data_container)
        quant_cols = [col for col in self.data_container.z_scores.columns if col not in [('batch', '', ''), ('Compound', '', ''),('screen', '', '')]]
        test_sum = self.data_container.z_scores[quant_cols].sum().sum() # Sum ALL z scores
        self.assertAlmostEqual(test_sum, self.true_sum, 8)

    def test_melt_z_score(self):
        self.p.process_and_normalize(self.data_container)
        self.z.compute_z_score(self.data_container)
        self.z.melt_z_score_df(self.data_container)
        test_sum = self.data_container.melted_z_scores["Z Score"].sum() # Sum ALL z scores
        self.assertAlmostEqual(test_sum, self.true_sum, 8)

class TestDataLoader(unittest.TestCase):

    test_pg_path = os.path.join(os.getcwd(), "test", "test_pg_matrix.csv")
    test_pr_path = os.path.join(os.getcwd(), "test", "test_pr_matrix.csv")

    def setUp(self):
        self.dl = DataLoader()

    def test_detect_file_format(self):
        self.assertEqual(self.dl._detect_file_format(self.test_pg_path), "csv")
        self.assertEqual(self.dl._detect_file_format("fake_test_path.tsv"), "tsv")
        with self.assertRaises(ValueError):
            self.dl._detect_file_format("bad_path.xyz")
    
    def test_load_lazy_df(self):
        df = self.dl._load_lazy_df(self.test_pg_path)
        self.assertIsInstance(df, pl.lazyframe.frame.LazyFrame)
    
    def test_load_data(self):
        data_container = self.dl.load_data(self.test_pg_path)
        self.assertEqual(data_container.filetype, "diann")
        self.assertIsInstance(data_container, DataContainer)
        self.assertIsInstance(data_container.raw_df, pd.core.frame.DataFrame)
        self.assertEqual(data_container.raw_df.shape, (100, 578))
        data_container = self.dl.load_data(self.test_pr_path)
        self.assertIsInstance(data_container.raw_df, pd.core.frame.DataFrame)
        self.assertEqual(data_container.raw_df.shape, (10, 579))

class TestProcessUtils(unittest.TestCase):

    def setUp(self):
        self.p = ProcessUtils()
    
    def test_load_tf_list(self):
        tf_list = self.p.load_tf_list()
        self.assertEqual(len(tf_list), 1327)
        self.assertEqual(tf_list, self.p.tf_list)
        testp = ProcessUtils(label_tfs=False)
        self.assertNotIsInstance(testp.tf_list, list)
    
    def test_load_gene_info(self):
        gene_dict = self.p.load_gene_info()
        self.assertEqual(len(gene_dict.keys()), 82861)

    def test_split_batch_screen(self):
        data = {
                'batch': ['SET1REP1_screen1', 'SET2REP2_screen2', 'SET3REP3_screen3'],
                'some_other_column': [1, 2, 3]
                }
        df = pd.DataFrame(data)
        result = self.p._split_batch_screen(df)
        expected_df = pd.DataFrame({
                                    'batch': ['SET1REP1', 'SET2REP2', 'SET3REP3'],
                                    'some_other_column': [1, 2, 3],
                                    'screen': ['screen1', 'screen2', 'screen3'],
                                    })
        result = result.reset_index(drop=True)
        expected_df = expected_df.reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_get_screen(self):
        self.assertEqual(self.p._get_screen('MSR5863_SET10REP2C3_TAL123_DIA.d'), "Anborn")
        self.assertEqual(self.p._get_screen('MSR8000_SET10REP2C3_TAL123_DIA.d'), "Anborn")
        self.assertEqual(self.p._get_screen('MSR12_SET10REP2C3_TAL123_DIA.d'), "THP-1 1K")
        with self.assertRaises(KeyError):
            self.p._get_screen('NOTASCREEN_SET10REP2C3_TAL123_DIA.d')

        # Test with new screen dict
        custom_screen_split = {(0, 100): "Screen A",  
                               (100, 1e16): "Screen B",
                               "ScreenName": "Screen C"}
        p = ProcessUtils(screen_split=custom_screen_split)
        self.assertEqual(p.screen_split, custom_screen_split)
        self.assertEqual(p._get_screen('MSR100_SET10REP2C3_TAL123_DIA.d'), "Screen B")
        self.assertEqual(p._get_screen('MSR50_SET10REP2C3_TAL123_DIA.d'), "Screen A")
        self.assertEqual(p._get_screen('MSR102_SET10REP2C3_TAL123_DIA.d'), "Screen B")
        self.assertEqual(p._get_screen('ScreenName_SET10REP2_TAL123_DIA.d'), "Screen C")
        
        # Test with missing MSR values
        with self.assertRaises(ValueError):
            p = ProcessUtils(screen_split={(0, 99): "Screen A",  # MSR numbers by which to split screens
                                       (100, 1e16): "Screen B"})

        
    def test_get_compound_name(self):
        compounds = ['MSR5863_SET10REP2C3_TAL123_DIA.d',
                     'MSR12_SET9REP14C3_TAL0000981_DIA.d',
                     'MSR10000_SET12REP3C3_TAL1052_DIA.d',
                     'MSR275_SET14REP15C3_FRA00012_DIA.d',
                     'MSR5864_SET14REP15C3_DMSO_DIA.d',
                     'MSR123_SET14REP15C3_NUC1_DIA.d',
                     'MSR5864_SET14REP15C3_NUC_DIA.d',
                     'MSR583_SET14REP15C3_DBET6_DIA.d',
                     'MSR674_SET14REP15C3_NONE_DIA.d']
        expected = ["TAL123",
                    "TAL981",
                    "TAL1052",
                    "FRA",
                    "DMSO",
                    "NUC1",
                    "NUC",
                    "dBET6",
                    "None"]
        result = [self.p._get_compound_name(s) for s in compounds]
        self.assertEqual(expected, result)
        with self.assertRaises(Exception):
            self.p._get_compound_name('MSR674_SET14REP15C3_INVALIDCOMPOUND_DIA.d')

    def test_get_batch_compound_names(self):
        data = {
            'Compound': ['MSR5863_SET10REP2C3_TAL123_DIA.d',
                         'MSR12_SET9REP14C3_TAL0000981_DIA.d',
                         'MSR10000_SET12REP3C3_TAL1052_DIA.d',
                         'MSR5864_SET14REP15C3_FRA00012_DIA.d'],
            'Other_Column': [1, 2, 3, 4]
        }
        pivot_df = pd.DataFrame(data).reset_index(drop=True)

        expected_df = pd.DataFrame({
            'Compound': ["TAL123", "TAL981", "TAL1052", "FRA"],
            'Other_Column': [1, 2, 3, 4],
            'batch': ['SET10REP2_Anborn', 
                      'SET9REP14_THP-1 1K',
                      'SET12REP3_Anborn',
                      'SET14REP15_Anborn']
        })

        result = self.p._get_batch_compound_names(pivot_df)

        result = result.reset_index(drop=True)
        expected_df = expected_df.reset_index(drop=True)

        pd.testing.assert_frame_equal(result, expected_df)

class TestPeptideProcessor(unittest.TestCase):

    test_pr_path = os.path.join(os.getcwd(), "test", "test_pr_matrix.csv")
    test_pg_path = os.path.join(os.getcwd(), "test", "test_pg_matrix.csv")

    def setUp(self):
        self.pep_proc = PeptideProcessor(dropna_percent_threshold=100)

    def test_process_and_normalize(self):
        data = {
            ('batch', '', ''): ['SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1'],
            ('Compound', '', ''): ['FRA', 'FRA', 'FRA', 'TAL281', 'TAL1432'],
            ('P37108', 'SRP14_False', 'AAAAAAAAAPAAAATAPTTAATTAATAAQ3'): [-1.259301, None, -1.399689, 0.235722, 0.034296],
            ('Q96JP5;Q96JP5-2', 'ZFP91_False', 'AAAAAAAAAVSR2'): [None, 1.220315, None, 1.883378, 1.644666],
            ('P36578', 'RPL4_False', 'AAAAAAALQAK2'): [4.271176, 4.997890, 4.730296, 4.594354, 4.698532],
            ('Q6SPF0', 'SAMD1_False', 'AAAAAATAPPSPGPAQPGPR2'): [-0.048668, -0.452178, -0.167983, -0.884466, None],
            ('Q8WUQ7;Q8WUQ7-2', 'CACTIN_True', 'AAAAALSQQQSLQER2'): [0.530404, 0.328163, 0.338736, 0.115737, 0.264015],
            ('Q9P258', 'RCC2_False', 'AAAAAWEEPSSGNGTAR2'): [1.659520, 2.074172, 1.756539, 1.406870, 1.164262],
            ('Q9UPT8', 'ZC3H4_False', 'AAAAPAATTATPPPEGAPPQPGVHNLPVPTLFGTVK4'): [None, -2.387604, None, None, -0.482742],
            ('Q68DK7', 'MSL1_False', 'AAAAPAGGNPEQR2'): [None, None, None, -0.329615, None],
            ('Q96L91;Q96L91-2;Q96L91-3;Q96L91-5', 'EP400_False', 'AAAAPFQTSQASASAPR2'): [None, None, None, -0.396926, -0.130211],
            ('P52701;P52701-2;P52701-3', 'MSH6_False', 'AAAAPGASPSPGGDAAWSEAGPGPRPLAR3'): [-1.501962, None, None, None, None],
            ('screen', '', ''): ['Anborn', 'Anborn', 'Anborn', 'Anborn', 'Anborn'],
        }

        multi_index = pd.MultiIndex.from_tuples([
            ('batch', '', ''),
            ('Compound', '', ''),
            ('P37108', 'SRP14_False', 'AAAAAAAAAPAAAATAPTTAATTAATAAQ3'),
            ('Q96JP5;Q96JP5-2', 'ZFP91_False', 'AAAAAAAAAVSR2'),
            ('P36578', 'RPL4_False', 'AAAAAAALQAK2'),
            ('Q6SPF0', 'SAMD1_False', 'AAAAAATAPPSPGPAQPGPR2'),
            ('Q8WUQ7;Q8WUQ7-2', 'CACTIN_True', 'AAAAALSQQQSLQER2'),
            ('Q9P258', 'RCC2_False', 'AAAAAWEEPSSGNGTAR2'),
            ('Q9UPT8', 'ZC3H4_False', 'AAAAPAATTATPPPEGAPPQPGVHNLPVPTLFGTVK4'),
            ('Q68DK7', 'MSL1_False', 'AAAAPAGGNPEQR2'),
            ('Q96L91;Q96L91-2;Q96L91-3;Q96L91-5', 'EP400_False', 'AAAAPFQTSQASASAPR2'),
            ('P52701;P52701-2;P52701-3', 'MSH6_False', 'AAAAPGASPSPGGDAAWSEAGPGPRPLAR3'),
            ('screen', '', '')
        ], names=['Protein.Ids', 'Genes', 'Precursor.Id'])


        expected_df = pd.DataFrame(data)
        expected_df.columns = multi_index

        quant_cols = [col for col in expected_df.columns if col not in [('batch', '', ''), ('Compound', '', ''),('screen', '', '')]]
        expected_df[quant_cols] = expected_df[quant_cols].astype(float)

        dl = DataLoader()
        data_container = dl.load_data(self.test_pr_path)
        self.pep_proc.process_and_normalize(data_container)
        result = data_container.normalized_df

        pd.testing.assert_frame_equal(result.iloc[:5], expected_df)
        try:
            pd.testing.assert_frame_equal(data_container.raw_df, data_container.normalized_df) # Test that raw df is not overwritten
            raise AssertionError("DataFrames are unexpectedly equal.")
        except AssertionError:
            pass  # This is expected behavior

        # Test inheritance of the screen identifier
        custom_screen_split = {(0, 100): "Screen A",  
                                (100, 1e16): "Screen B"}
        p = PeptideProcessor(screen_split=custom_screen_split)
        self.assertEqual(p.screen_split, custom_screen_split)
        self.assertEqual(p._get_screen('MSR100_SET10REP2C3_TAL123_DIA.d'), "Screen B")
        self.assertEqual(p._get_screen('MSR50_SET10REP2C3_TAL123_DIA.d'), "Screen A")
        self.assertEqual(p._get_screen('MSR102_SET10REP2C3_TAL123_DIA.d'), "Screen B")

        # Test that it ignores screens when instructed
        p = PeptideProcessor(label_screens=False)
        p.process_and_normalize(data_container)
        self.assertTrue("screen" not in data_container.raw_df.columns)

        # Test error handling for wrong file
        with self.assertRaises(ValueError):
            data_container = dl.load_data(self.test_pg_path)
            data = data_container.raw_df
            p.process_and_normalize(data_container)
        
class TestProteinProcessor(unittest.TestCase):
    test_pg_path = os.path.join(os.getcwd(), "test", "test_pg_matrix.csv")
    test_pr_path = os.path.join(os.getcwd(), "test", "test_pr_matrix.csv")

    def setUp(self):
        self.prot_proc = ProteinProcessor()

    def test_process_and_normalize(self):
        data = {
            'Genes': ['A2ML1', 'A2ML1', 'A2ML1', 'A2ML1', 'A2ML1'],
            'batch': ['SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1'],
            'Protein.Ids': ['A8K2U0', 'A8K2U0', 'A8K2U0', 'A8K2U0', 'A8K2U0'],
            'Compound': ['TAL281', 'TAL153', 'TAL750', 'TAL1045', 'TAL369'],
            'Abundance': [-0.268770, 0.237281, 0.731664, -0.524845, -0.662243],
            'Is TF': [False]*5,
            'screen': ['Anborn', 'Anborn', 'Anborn', 'Anborn', 'Anborn']
        }

        expected_df = pd.DataFrame(data)

        dl = DataLoader()
        data_container = dl.load_data(self.test_pg_path)
        self.prot_proc.process_and_normalize(data_container)
        result = data_container.normalized_df

        pd.testing.assert_frame_equal(result.iloc[:5], expected_df)

        # Test that some TFs are labels
        tf_df = result.loc[result["Is TF"]]
        self.assertEqual(tf_df.shape[0], 3234)

        # Test inheritance of the screen identifier
        custom_screen_split = {(0, 100): "Screen A",  
                                (100, 1e16): "Screen B"}
        p = ProteinProcessor(screen_split=custom_screen_split)
        self.assertEqual(p.screen_split, custom_screen_split)
        self.assertEqual(p._get_screen('MSR100_SET10REP2C3_TAL123_DIA.d'), "Screen B")
        self.assertEqual(p._get_screen('MSR50_SET10REP2C3_TAL123_DIA.d'), "Screen A")
        self.assertEqual(p._get_screen('MSR102_SET10REP2C3_TAL123_DIA.d'), "Screen B")


        # Test that it ignores screens when instructed
        p = ProteinProcessor(label_screens=False, label_tfs=False)
        p.process_and_normalize(data_container)
        df = data_container.normalized_df
        self.assertTrue("screen" not in df.columns)
        self.assertTrue("Is TF" not in df.columns)

        # Test error handling for wrong file
        with self.assertRaises(ValueError):
            data_container = dl.load_data(self.test_pr_path)
            p.process_and_normalize(data_container)

class TestProteinZScoreCalculator(unittest.TestCase):

    test_pg_path = os.path.join(os.getcwd(), "test", "test_pg_matrix.csv")
    test_pr_path = os.path.join(os.getcwd(), "test", "test_pr_matrix.csv")

    def setUp(self):
        self.dl  = DataLoader()
        self.prot_proc = ProteinProcessor()
        self.data_container = self.dl.load_data(self.test_pg_path)
        self.prot_proc.process_and_normalize(self.data_container)
        self.z = ProteinZScoreCalculator()
    
    def test_compute_z_score(self):
        self.z.compute_z_score(self.data_container)

        data = {
            'screen': ["Anborn"] *5,
            'Genes': ['A2ML1', 'A2ML1', 'A2ML1', 'A2ML1', 'A2ML1'],
            'batch': ['SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1'],
            'Protein.Ids': ['A8K2U0', 'A8K2U0', 'A8K2U0', 'A8K2U0', 'A8K2U0'],
            'Compound': ['TAL281', 'TAL153', 'TAL750', 'TAL1045', 'TAL369'],
            'Abundance': [-0.268770, 0.237281, 0.731664, -0.524845, -0.662243],
            'Is TF' : [False]*5,
            'Z Score': [-0.770911, 0.680591, 2.098623, -1.505407, -1.899505],
            'med Z Score': [-0.770911, -0.295842, 2.098623, -1.505407, -1.899505]
        }

        expected_df = pd.DataFrame(data)
        z_score = self.data_container.z_scores

        pd.testing.assert_frame_equal(z_score.iloc[:5], expected_df)

        # Test error handling
        data_container = self.dl.load_data(self.test_pr_path)
        pp = PeptideProcessor()
        pp.process_and_normalize(data_container)
        with self.assertRaises(ValueError):
            self.z.compute_z_score(data_container)

        # Test calculating without screen data
        self.data_container.normalized_df = self.data_container.normalized_df.drop(columns=["screen"])
        self.z.compute_z_score(self.data_container)
        expected_df = expected_df.drop(columns=["screen"])
        pd.testing.assert_frame_equal(self.data_container.z_scores.iloc[:5], expected_df)

class TestPeptideZScoreCalculator(unittest.TestCase):
    test_pg_path = os.path.join(os.getcwd(), "test", "test_pg_matrix.csv")
    test_pr_path = os.path.join(os.getcwd(), "test", "test_pr_matrix.csv")

    def setUp(self):
        self.dl  = DataLoader()
        self.pep_proc = PeptideProcessor(dropna_percent_threshold=100)
        self.data_container = self.dl.load_data(self.test_pr_path)
        self.pep_proc.process_and_normalize(self.data_container)
        self.z = PeptideZScoreCalculator()

    def test_calculate_z_score(self):
        data = {
            ('batch', '', ''): ['SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1'],
            ('Compound', '', ''): ['FRA', 'FRA', 'FRA', 'TAL281', 'TAL1432'],
            ('P37108', 'SRP14_False', 'AAAAAAAAAPAAAATAPTTAATTAATAAQ3'): [-0.633648, None, -0.817097, 1.319951, 1.056741],
            ('Q96JP5;Q96JP5-2', 'ZFP91_False', 'AAAAAAAAAVSR2'): [None, -0.194224, None, 1.384308, 0.816015],
            ('P36578', 'RPL4_False', 'AAAAAAALQAK2'): [-0.144179, 1.927473, 1.164640, 0.777109, 1.074089],
            ('Q6SPF0', 'SAMD1_False', 'AAAAAATAPPSPGPAQPGPR2'): [1.519493, 0.481067, 1.212439, -0.631415, None],
            ('Q8WUQ7;Q8WUQ7-2', 'CACTIN_True', 'AAAAALSQQQSLQER2'): [-0.248740, -1.179475, -1.130815, -2.157081, -1.474688],
            ('Q9P258', 'RCC2_False', 'AAAAAWEEPSSGNGTAR2'): [-0.142098, 1.157632, 0.162009, -0.934032, -1.694490],
            ('Q9UPT8', 'ZC3H4_False', 'AAAAPAATTATPPPEGAPPQPGVHNLPVPTLFGTVK4'): [None, -3.852793, None, None, 1.648315],
            ('Q68DK7', 'MSL1_False', 'AAAAPAGGNPEQR2'): [None, None, None, 1.614477, None],
            ('Q96L91;Q96L91-2;Q96L91-3;Q96L91-5', 'EP400_False', 'AAAAPFQTSQASASAPR2'): [None, None, None, -3.155988, -1.981292],
            ('P52701;P52701-2;P52701-3', 'MSH6_False', 'AAAAPGASPSPGGDAAWSEAGPGPRPLAR3'): [0.062269, None, None, None, None],
            ('screen', '', ''): ['Anborn', 'Anborn', 'Anborn', 'Anborn', 'Anborn']
        }

        multi_index = pd.MultiIndex.from_tuples([
            
            ('screen', '', ''),
            ('batch', '', ''),
            ('Compound', '', ''),
            ('P37108', 'SRP14_False', 'AAAAAAAAAPAAAATAPTTAATTAATAAQ3'),
            ('Q96JP5;Q96JP5-2', 'ZFP91_False', 'AAAAAAAAAVSR2'),
            ('P36578', 'RPL4_False', 'AAAAAAALQAK2'),
            ('Q6SPF0', 'SAMD1_False', 'AAAAAATAPPSPGPAQPGPR2'),
            ('Q8WUQ7;Q8WUQ7-2', 'CACTIN_True', 'AAAAALSQQQSLQER2'),
            ('Q9P258', 'RCC2_False', 'AAAAAWEEPSSGNGTAR2'),
            ('Q9UPT8', 'ZC3H4_False', 'AAAAPAATTATPPPEGAPPQPGVHNLPVPTLFGTVK4'),
            ('Q68DK7', 'MSL1_False', 'AAAAPAGGNPEQR2'),
            ('Q96L91;Q96L91-2;Q96L91-3;Q96L91-5', 'EP400_False', 'AAAAPFQTSQASASAPR2'),
            ('P52701;P52701-2;P52701-3', 'MSH6_False', 'AAAAPGASPSPGGDAAWSEAGPGPRPLAR3'),
        ], names=['Protein.Ids', 'Genes', 'Precursor.Id'])

        expected_df = pd.DataFrame(data, columns=multi_index)

        self.z.compute_z_score(self.data_container)
        z_scores = self.data_container.z_scores

        pd.testing.assert_frame_equal(z_scores.iloc[:5], expected_df)

        # Test error handling
        data_container = self.dl.load_data(self.test_pg_path)
        pp = ProteinProcessor()
        pp.process_and_normalize(data_container)
        with self.assertRaises(ValueError):
            self.z.compute_z_score(data_container)

        # Test calculating without screen data
        self.data_container.normalized_df = self.data_container.normalized_df.drop(columns=["screen"])
        self.z.compute_z_score(self.data_container)
        result = self.data_container.z_scores
        expected_df = expected_df.drop(columns=["screen"])
        pd.testing.assert_frame_equal(result.iloc[:5], expected_df)

    # def test_get_median_z_score(self):
    #     data = {
    #         ('screen', '', ''): ['Anborn', 'Anborn', 'Anborn', 'Anborn', 'Anborn'],
    #         ('Compound', '', ''): ['DMSO', 'FRA', 'TAL1025', 'TAL1035', 'TAL1036'],
    #         ('P37108', 'SRP14_False', 'AAAAAAAAAPAAAATAPTTAATTAATAAQ3'): [-0.5334404597266602, -1.065759928730299, -1.14072170539318, -1.1491300791676362, 0.7934110550949246],
    #         ('Q96JP5;Q96JP5-2', 'ZFP91_False', 'AAAAAAAAAVSR2'): [0.010751789897853276, -1.3941499110509465, -1.4619871104404696, -1.7771470859195677, 0.2951661994836766],
    #         ('P36578', 'RPL4_False', 'AAAAAAALQAK2'): [-0.08901027512310429, 0.18773835192781038, -1.7527948875349475, -2.748797162058653, 0.4322621634948626],
    #         ('Q6SPF0', 'SAMD1_False', 'AAAAAATAPPSPGPAQPGPR2'): [0.30054259069394285, -0.052905785507017494, -0.26482233093935587, 1.116107963009016, -2.934392700758811],
    #         ('Q8WUQ7;Q8WUQ7-2', 'CACTIN_True', 'AAAAALSQQQSLQER2'): [-0.2698689815435681, 1.6589867932303823, 0.34527420814361953, 1.2045920625074742, -0.23144935753882287],
    #         ('Q9P258', 'RCC2_False', 'AAAAAWEEPSSGNGTAR2'): [0.22423292436539943, -0.846004020837186, 0.9249935779133865, 0.3857646051171687, -1.7044456467273803],
    #         ('Q9UPT8', 'ZC3H4_False', 'AAAAPAATTATPPPEGAPPQPGVHNLPVPTLFGTVK4'): [-0.06374910333421302, -2.941365586022088, -0.23130436913780278, -0.10268224834794583, 0.3246818145759337],
    #         ('Q68DK7', 'MSL1_False', 'AAAAPAGGNPEQR2'): [0.20173751892825315, None, -1.0820230224411604, -0.8993800988528352, 2.3200731275682895],
    #         ('Q96L91;Q96L91-2;Q96L91-3;Q96L91-5', 'EP400_False', 'AAAAPFQTSQASASAPR2'): [0.014440016001873753, -7.402101520381838, -0.0726318618271808, 1.563459708454522, -0.5600934040856896],
    #         ('P52701;P52701-2;P52701-3', 'MSH6_False', 'AAAAPGASPSPGGDAAWSEAGPGPRPLAR3'): [0.7226367290294418, -0.7149719326926692, 0.4589032324230374, 0.0746398178336411, None],
    #     }

    #     multi_index = pd.MultiIndex.from_tuples(
    #         [('screen', '', ''),
    #         ('Compound', '', ''),
    #         ('P37108', 'SRP14_False', 'AAAAAAAAAPAAAATAPTTAATTAATAAQ3'),
    #         ('Q96JP5;Q96JP5-2', 'ZFP91_False', 'AAAAAAAAAVSR2'),
    #         ('P36578', 'RPL4_False', 'AAAAAAALQAK2'),
    #         ('Q6SPF0', 'SAMD1_False', 'AAAAAATAPPSPGPAQPGPR2'),
    #         ('Q8WUQ7;Q8WUQ7-2', 'CACTIN_True', 'AAAAALSQQQSLQER2'),
    #         ('Q9P258', 'RCC2_False', 'AAAAAWEEPSSGNGTAR2'),
    #         ('Q9UPT8', 'ZC3H4_False', 'AAAAPAATTATPPPEGAPPQPGVHNLPVPTLFGTVK4'),
    #         ('Q68DK7', 'MSL1_False', 'AAAAPAGGNPEQR2'),
    #         ('Q96L91;Q96L91-2;Q96L91-3;Q96L91-5', 'EP400_False', 'AAAAPFQTSQASASAPR2'),
    #         ('P52701;P52701-2;P52701-3', 'MSH6_False', 'AAAAPGASPSPGGDAAWSEAGPGPRPLAR3')]
    #         , names=['Protein.Ids', 'Genes', 'Precursor.Id'])

    #     expected_df = pd.DataFrame(data, columns=multi_index)

    #     self.z.compute_z_score(self.data_container)
    #     self.z.get_median_z_score(self.data_container)
    #     result = self.data_container.median_z_scores
    #     pd.testing.assert_frame_equal(result.iloc[:5], expected_df)
    
    def test_melt_z_score_df(self):
        data = {
            'screen': ['Anborn', 'Anborn', 'Anborn', 'Anborn', 'Anborn'],
            'batch': ['SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1', 'SET1REP1'],
            'Compound': ['FRA', 'FRA', 'FRA', 'TAL281', 'TAL1432'],
            'Z Score': [-0.633648, np.nan, -0.817097, 1.319951, 1.056741],
            'Protein.Ids': ['P37108', 'P37108', 'P37108', 'P37108', 'P37108'],
            'Genes': ['SRP14', 'SRP14', 'SRP14', 'SRP14', 'SRP14'],
            'Is TF': [False]*5,
            'Precursor.Id': ['AAAAAAAAAPAAAATAPTTAATTAATAAQ3'] * 5,
            'med Z Score': [-1.065760]*3 + [1.260673, 1.056741]
        }

        expected_df = pd.DataFrame(data)

        self.z.compute_z_score(self.data_container)
        self.z.melt_z_score_df(self.data_container)
        result = self.data_container.melted_z_scores
        pd.testing.assert_frame_equal(result.iloc[:5], expected_df)



if __name__ == '__main__':
    unittest.main(warnings="ignore")