from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 1485760:
        raise ValidationError("El tamaño máximo de la foto debe ser de 1 MB")
    else:
        return value
