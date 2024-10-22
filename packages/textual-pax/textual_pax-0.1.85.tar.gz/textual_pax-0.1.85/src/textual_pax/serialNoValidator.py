from textual.validation import Function, Number, ValidationResult, Validator

EXAMPLES = [{'Model': 'A920', 'ExampleSerialNo': '0821674609'}, {'Model': 'A920Pro', 'ExampleSerialNo': '1851160310'}, {'Model': 'A35', 'ExampleSerialNo': '2290065118'}, {'Model': 'A60', 'ExampleSerialNo': '1350021966'}, {'Model': 'A77', 'ExampleSerialNo': '1760234077'}, {'Model': 'A80', 'ExampleSerialNo': '1240383205'}, {'Model': 'E500', 'ExampleSerialNo': '1150050557'}, {'Model': 'E600', 'ExampleSerialNo': '1190018657'}, {'Model': 'E700', 'ExampleSerialNo': '1340004658'}, {'Model': 'E600M', 'ExampleSerialNo': '2270008806'}, {'Model': 'Q10A', 'ExampleSerialNo': '2400004913'}, {'Model': 'Q20L', 'ExampleSerialNo': '1140077754'}, {'Model': 'D135', 'ExampleSerialNo': '1890200678'}, {'Model': 'S300', 'ExampleSerialNo': '5G047654'}, {'Model': 'SP30', 'ExampleSerialNo': '3L013509'}]

class SerialNoValidator(Validator):
    def validate(self, value: str) -> ValidationResult:
        
        if value in ["0000", "BKSPC"]:
            return self.success()
        if self.is_serialNo(value):
            return self.success()
        else:
            return self.failure("Invalid Entry")

    @staticmethod
    def is_serialNo(value: str) -> bool:
        """Checks if the given value is a valid serial number.

        Args:
            value (str): The value to check.
            examples (list[dict]): A list of dictionaries containing 'ExampleSerialNo' keys.

        Returns:
            bool: True if the value is a valid serial number, False otherwise.
        """
        
        # Ensure length is between 8 and 10 characters
        if not (8 <= len(value) <= 10):
            return False
        
        # Check first three digits against examples
        for example in EXAMPLES:
            if value[:3] == example['ExampleSerialNo'][:3]:
                return True
            
        # If no match found, return False
        return False


"""def validTest():
    
    check = SerialNoValidator()
    thing = check.validate('0821674609')
    print(thing.is_valid)

validTest()"""