html = '''
<head>
    <title>Proposta Comercial</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #FFFFFF;
        }

        .container {
            width: 90%;
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .header {
            text-align: center;
            margin-bottom: 20px;
        }

        .header h1 {
            color: #333;
        }

        .invoice-details {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .invoice-details div {
            width: 100%;
            margin-bottom: 10px;
        }

        .invoice-details h4 {
            margin: 5px 0;
            color: #555;
        }

        .invoice-table {
            width: 100%;
            border-collapse: collapse;
            border-spacing: 10px;
        }

        .invoice-table th,
        .invoice-table td {
            padding: 24px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        .invoice-table th {
            background-color: #f5f5f5;
            color: #4E44AC; /* Adicionando roxo ao texto do cabeçalho */
            font-size: 18px; /* Aumentando o tamanho do texto do cabeçalho */
        }

        .invoice-table td.quantity,
        .invoice-table td.price {
            text-align: right;
        }

        .invoice-total {
            margin-top: 20px;
            text-align: right;
        }

        .invoice-total h3 {
            color: #333;
        }

        @media screen and (min-width: 600px) {
            .invoice-details div {
                width: 48%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="color: #4E44AC;">Proposta Comercial</h1> <!-- Adicionando roxo ao título -->
        </div>

        <div class="invoice-details">
            <div>
                <h4 style="color: #4E44AC;">De:</h4> <!-- Adicionando roxo ao subtítulo -->
                <p>Rentbrella Brasil LTDA</p>
                <p>Avenida Angelica, 2447, 10º andar</p>
                <p>Bela Vista, São Paulo, SP, 01227-200</p>
            </div>
            <div>
                <h4 style="color: #4E44AC;">Para:</h4> <!-- Adicionando roxo ao subtítulo -->
                <p>Nome do Cliente</p>
                <p>Cidade do Cliente, Estado, CEP</p>
            </div>
        </div>

        <table class="invoice-table">
            <thead>
                <tr>
                    <th>Local</th>
                    <th>Item</th>
                    <th>Unidades</th>
                    <th>Valor Unitário</th>
                    <th>Tipo de Cobrança</th>
                </tr>
            </thead>
'''
filters = [
    Filter('proposta', recordData['id_0nu7_jf161h_sdadu7wsy'], "==", 'string'),
]
result = jestor.table('_sipnkkigdgcw4owu1s0l').get(filters)

for item in result:
    html = html + '''<tr><td>''' + item['cidade'] + '</td><td>' + item['item'] + '</td><td>' + "{:.0f}".format(item['quantidade']) + '</td><td>R$' + "{:.2f}".format(item['valor_unitario']) + '</td><td>' + item['tipo_de_cobranca'] + '</td></tr>'

html = html + '</table>'

pdf = jestor.generatePDF([html, "A4", "landscape"])
files = jestor.file('0nu7_jf161h_sdadu7wsy')
files.add({'name': 'file_test', 'localFile': pdf})

result = jestor.table('0nu7_jf161h_sdadu7wsy').update(recordData['id_0nu7_jf161h_sdadu7wsy'], {'proposta': files.toJson()})
result = jestor.table('0nu7_jf161h_sdadu7wsy').update(recordData['id_0nu7_jf161h_sdadu7wsy'], {'status': 'Criado'})
