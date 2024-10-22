import unittest
from hyrule_shield.anonymizer import anonymize_message_spacy

class TestAnonymizer(unittest.TestCase):
    def test_anonymize_person_name(self):
        message = "Meu nome é Carlos Eduardo, meu CPF é 111.222.333-44."
        expected_output = "Meu nome é <PER>, meu CPF é <CPF>."
        result = anonymize_message_spacy(message)
        self.assertEqual(result, expected_output)

    def test_anonymize_company_name(self):
        message = "A empresa Tech Solutions Ltda está localizada na Avenida Paulista, 1000, São Paulo, SP."
        expected_output = "A empresa <ORG> está localizada na <ENDERECO>, São <PER>, SP."
        result = anonymize_message_spacy(message)
        self.assertEqual(result, expected_output)

    def test_anonymize_cnpj(self):
        message = "Nosso CNPJ é 12.345.678/0001-90."
        expected_output = "Nosso CNPJ é <CNPJ>."
        result = anonymize_message_spacy(message)
        self.assertEqual(result, expected_output)

    def test_anonymize_address(self):
        message = "Estamos localizados na Rua das Américas, 123, Rio de Janeiro, RJ. CEP 20000-000."
        expected_output = "Estamos localizados na <ENDERECO>, Rio de Janeiro, RJ. CEP <CEP>."
        result = anonymize_message_spacy(message)
        self.assertEqual(result, expected_output)

    def test_no_anonymization_needed(self):
        message = "Gostaria de saber o prazo para entrega dos produtos."
        expected_output = "Gostaria de saber o prazo para entrega dos produtos."
        result = anonymize_message_spacy(message)
        self.assertEqual(result, expected_output)

    def test_bulk_anonymization(self):
        test_cases = [
            ("Meu nome é João Silva e meu CPF é 123.456.789-00.", "Meu nome é <PER> e meu CPF é <CPF>."),
            ("A empresa XYZ S.A. está localizada na Avenida Brasil, 1000, Belo Horizonte, MG.", "A empresa <ORG> está localizada na <ENDERECO>, Belo Horizonte, MG."),
            ("Entre em contato pelo telefone (11) 98765-4321.", "Entre em contato pelo telefone <TELEFONE>."),
            ("Nosso CNPJ é 98.765.432/0001-22.", "Nosso CNPJ é <CNPJ>."),
            ("Estamos na Travessa das Flores, 45, Curitiba, PR. CEP 80000-000.", "Estamos na <ENDERECO>, Curitiba, PR. CEP <CEP>."),
            ("Olá, sou Maria e gostaria de saber o prazo de entrega.", "Olá, sou <PER> e gostaria de saber o prazo de entrega."),
            ("Gostaria de confirmar se o CNPJ 23.123.456/0001-00 está ativo.", "Gostaria de confirmar se o CNPJ <CNPJ> está ativo."),
            ("Aqui é o João, meu RG é 12.345.678-9.", "Aqui é o <PER>, meu RG é <RG>."),
            ("Favor depositar na conta bancária usando o CPF 111.222.333-44.", "Favor depositar na conta bancária usando o CPF <CPF>."),
            ("Bom dia, estou entrando em contato para saber mais sobre os serviços.", "Bom dia, estou entrando em contato para saber mais sobre os serviços.")
        ]

        for message, expected_output in test_cases:
            with self.subTest(message=message):
                result = anonymize_message_spacy(message)
                self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
