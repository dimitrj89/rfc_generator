from rfc_generator import RFC_PF, RFC_PM

rfc_pf = RFC_PF(nombres="Dimitrj",apellido_paterno="Bonansea",fecha_nacimiento="1989-06-10")
print(rfc_pf.generate())

rfc_pm = RFC_PM(nombre_empresa="Champion Mexicana de Bujías, S.A.",fecha_constitucion="1983-07-02")
print(rfc_pm.generate())