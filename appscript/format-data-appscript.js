function copyAndFormatData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sourceSheet = ss.getSheetByName('native');
  var targetSheet = ss.getSheetByName('clean_data');

  // Obter os dados da aba "native" das colunas "A" até "P"
  var data = sourceSheet.getRange('A2:P' + sourceSheet.getLastRow()).getValues();
  Logger.log('Dados obtidos da aba "native": ' + data.length);

  // Processar os dados
  var processedData = data.map(function(row) {
    // Condição 1: Formatar a coluna B
    if (row[1] && row[1].toString().match(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/)) {
      var date = new Date(row[1]);
      row[1] = Utilities.formatDate(date, Session.getScriptTimeZone(), 'dd/MM/yyyy HH:mm:ss');
    }

    // Condição 2: Separar o nome completo na coluna M
    if (row[12] && row[12].toString().includes(' ')) {
      var nameParts = row[12].split(' ');
      row[12] = nameParts[0]; // Primeiro nome
      row.splice(13, 0, nameParts.slice(1).join(' ')); // Restante do nome na nova coluna N
    } else {
      row.splice(13, 0, ''); // Adicionar coluna N vazia se o nome for simples
    }

    // Condição 3: Formatar números de telefone na coluna N
    if (row[14]) {
      var phone = row[14].toString().replace(/[^0-9]/g, ''); // Remove caracteres não numéricos
      if (phone.length === 10 || phone.length === 11) {
        phone = '55' + phone; // Adiciona DDI se o número tiver 10 ou 11 dígitos
      }
      // Se o número tiver 12 ou 13 dígitos, não faz nada além de remover caracteres especiais
      row[14] = phone;
    }

    return row;
  });

  Logger.log('Dados processados: ' + processedData.length);

  // Verificar se há dados processados antes de colar na aba "clean_data"
  if (processedData.length > 0) {
    // Limpar a aba "clean_data" antes de colar os dados
    var lastRow = targetSheet.getLastRow();
    var lastColumn = targetSheet.getLastColumn();
    if (lastRow > 1 && lastColumn > 0) {
      targetSheet.getRange(2, 1, lastRow - 1, lastColumn).clearContent();
      Logger.log('Aba "clean_data" limpa.');
    } else {
      Logger.log('Aba "clean_data" já está vazia.');
    }

    // Colar os dados processados na aba "clean_data"
    targetSheet.getRange(2, 1, processedData.length, processedData[0].length).setValues(processedData);
    Logger.log('Dados colados na aba "clean_data".');
  } else {
    Logger.log('Nenhum dado processado para colar na aba "clean_data".');
  }
}