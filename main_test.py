import unittest
import requests, json
import pandas as pd
from main import get_endpoint_valuable_data, check_status_code_isOK, convert_json_to_dataframe, print_names_that_contains_5_or_more_vowels
from main import URL_ENDPOINT, OK_STATUS_CODE

class MainTest(unittest.TestCase):

    def test_get_endpoint_valuable_data(self):
        response_text, _ = get_endpoint_valuable_data()

        # Verifica se a resposta não está vazia
        self.assertIsNotNone(response_text)

        # Verifica se a resposta é uma string
        self.assertIsInstance(response_text, str)

         # Verifica se a resposta é um JSON válido|
        try:
            json_data = json.loads(response_text)
        except json.JSONDecodeError as e:
            self.fail(f"A resposta não é um JSON válido: {str(e)}")



    def test_check_status_code_isOK(self):
        # Testa o cenário em que o código de status é OK
        self.assertIsNone(check_status_code_isOK(OK_STATUS_CODE))

        # Testa o cenário em que o código de status é diferente de OK
        with self.assertRaises(requests.exceptions.RequestException):
            check_status_code_isOK(400)

    def test_convert_json_to_dataframe(self):
        # Dados de exemplo
        json_response = '''
        [
            {"id": 1, "name": "John", "email": "john@example.com"},
            {"id": 2, "name": "Jane", "email": "jane@example.com"}
        ]
        '''

        # Chamar a função de conversão
        df = convert_json_to_dataframe(json_response)

        # Verificar se os dados foram convertidos corretamente
        self.assertEqual(df.loc[1, 'name'], 'John')
        self.assertEqual(df.loc[2, 'email'], 'jane@example.com')

    def test_print_names_that_contains_5_or_more_vowels(self):
        # Cria um dataframe de exemplo
        data = {'name': ['Alice', 'Bob', 'Eve', 'Juuanilsoon', 'Isabellaaa']}
        df = pd.DataFrame(data)

        # Redireciona a saída de impressão para um objeto StringIO
        import io
        from contextlib import redirect_stdout
        output = io.StringIO()

        with redirect_stdout(output):
            print_names_that_contains_5_or_more_vowels(df)

        # Obtém a saída impressa
        printed_output = output.getvalue()

        # Verifica se a saída contém as informações corretas
        self.assertIn("Isabellaaa", printed_output)
        self.assertIn("Juuanilsoon", printed_output)
        self.assertNotIn("Alice", printed_output)
        self.assertNotIn("Bob", printed_output)
        self.assertNotIn("Eve", printed_output)

if __name__ == '__main__':
    unittest.main()
