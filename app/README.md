# RFC Generator
A package used to generate rfc for PF and PM given input information.

## How to use
_After installing the package use following import:_ <br>

**from rfc_generator import RFC_PF, RFC_PM**

_Then use following commands:_

**rfc_pf = RFC_PF(<br>**
    **&emsp;nombres='firstname and/or secondname', <br>**
    **&emsp;apellido_paterno='paternal_last_name', <br>**
    **&emsp;apellido_materno='maternal_last_name', [Optional] <br>** 
    **&emsp;fecha_nacimiento='birthdate' [format='YYYY-MM-DD'] <br>**
**)<br>**
**rfc = rfc_pf.generate()<br>**

_Or:_

**rfc_pm = RFC_PM(<br>**
    **&emsp;nombre_empresa='company name', <br>**
    **&emsp;fecha_constitucion='foundation date' [format='YYYY-MM-DD'] <br>**
**)<br>**
**rfc = rfc_pm.generate()<br>**