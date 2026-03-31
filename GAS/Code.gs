/**
 * Time University - 計測アプリ GAS バックエンド
 * スプレッドシートID: 1PIFem6XGPY0EBdMgSw0ei-fzZGfbm8gRMi8bxKgPjYM
 */

const SS_ID = '1PIFem6XGPY0EBdMgSw0ei-fzZGfbm8gRMi8bxKgPjYM';

function getOrCreateSheet(name) {
  const ss = SpreadsheetApp.openById(SS_ID);
  let sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
  }
  return sheet;
}

function setupSheets() {
  // sessions シート
  const sessions = getOrCreateSheet('sessions');
  if (sessions.getLastRow() === 0) {
    sessions.appendRow(['sessionId', 'workType', 'started', 'startTime', 'createdAt']);
  }

  // waiting シート
  const waiting = getOrCreateSheet('waiting');
  if (waiting.getLastRow() === 0) {
    waiting.appendRow(['sessionId', 'name', 'registeredAt']);
  }

  // results シート
  const results = getOrCreateSheet('results');
  if (results.getLastRow() === 0) {
    results.appendRow(['sessionId', 'name', 'workType', 'elapsedMs', 'targetMs', 'diffMs', 'diffSec', 'submittedAt']);
  }

  // assessments シート
  const assessments = getOrCreateSheet('assessments');
  if (assessments.getLastRow() === 0) {
    assessments.appendRow([
      'responseId', 'name', 'email', 'company', 'role', 'sessionId',
      'q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
      'q11','q12','q13','q14','q15','q16','q17','q18','q19','q20',
      'E','A','C','N','O',
      'z_E','z_A','z_C','z_N','z_O',
      'overScore','underScore','calibration','type',
      'submittedAt'
    ]);
  }
}

// ============================================
// Web App エントリーポイント
// ============================================

function doGet(e) {
  // POSTデータがGETパラメータ経由で来る場合の処理
  if (e.parameter.method === 'POST' && e.parameter.payload) {
    const data = JSON.parse(e.parameter.payload);
    return doPostInternal(data);
  }

  const action = e.parameter.action;
  let result;

  switch (action) {
    case 'status':
      result = getStatus(e.parameter.sessionId);
      break;
    case 'results':
      result = getResults(e.parameter.sessionId);
      break;
    case 'waiting':
      result = getWaiting(e.parameter.sessionId);
      break;
    default:
      result = { error: 'Unknown action: ' + action };
  }

  return ContentService.createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  let data;
  try {
    data = JSON.parse(e.postData.contents);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ error: 'Invalid JSON' }))
      .setMimeType(ContentService.MimeType.JSON);
  }
  return doPostInternal(data);
}

function doPostInternal(data) {
  const action = data.action;
  let result;

  switch (action) {
    case 'start':
      result = startSession(data);
      break;
    case 'register':
      result = registerParticipant(data);
      break;
    case 'result':
      result = saveResult(data);
      break;
    case 'reset':
      result = resetSession(data);
      break;
    case 'assessment':
      result = saveAssessment(data);
      break;
    default:
      result = { error: 'Unknown action: ' + action };
  }

  return ContentService.createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}

// ============================================
// Timer 機能
// ============================================

function startSession(data) {
  const sheet = getOrCreateSheet('sessions');
  const sessionId = data.sessionId;
  const workType = data.workType || '60sec';

  // 既存のセッション行を探す
  const rows = sheet.getDataRange().getValues();
  let found = false;
  for (let i = 1; i < rows.length; i++) {
    if (rows[i][0] === sessionId) {
      sheet.getRange(i + 1, 2).setValue(workType);
      sheet.getRange(i + 1, 3).setValue(true);
      sheet.getRange(i + 1, 4).setValue(new Date().getTime());
      found = true;
      break;
    }
  }

  if (!found) {
    sheet.appendRow([sessionId, workType, true, new Date().getTime(), new Date().toISOString()]);
  }

  return { success: true, started: true, startTime: new Date().getTime() };
}

function getStatus(sessionId) {
  const sheet = getOrCreateSheet('sessions');
  const rows = sheet.getDataRange().getValues();

  for (let i = 1; i < rows.length; i++) {
    if (rows[i][0] === sessionId) {
      return {
        started: rows[i][2] === true,
        startTime: rows[i][3],
        workType: rows[i][1]
      };
    }
  }

  return { started: false };
}

function registerParticipant(data) {
  const sheet = getOrCreateSheet('waiting');
  sheet.appendRow([data.sessionId, data.name, new Date().toISOString()]);
  return { success: true };
}

function getWaiting(sessionId) {
  const sheet = getOrCreateSheet('waiting');
  const rows = sheet.getDataRange().getValues();
  const participants = [];

  for (let i = 1; i < rows.length; i++) {
    if (rows[i][0] === sessionId) {
      participants.push({ name: rows[i][1] });
    }
  }

  return { participants: participants, count: participants.length };
}

function saveResult(data) {
  const sheet = getOrCreateSheet('results');
  const diffMs = data.elapsedMs - data.targetMs;
  const diffSec = Math.round(diffMs / 100) / 10; // 小数点1位

  sheet.appendRow([
    data.sessionId,
    data.name,
    data.workType,
    data.elapsedMs,
    data.targetMs,
    diffMs,
    diffSec,
    new Date().toISOString()
  ]);

  return { success: true, elapsed: Math.round(data.elapsedMs / 100) / 10, diff: diffSec };
}

function getResults(sessionId) {
  const sheet = getOrCreateSheet('results');
  const rows = sheet.getDataRange().getValues();
  const results = [];

  for (let i = 1; i < rows.length; i++) {
    if (rows[i][0] === sessionId) {
      results.push({
        name: rows[i][1],
        workType: rows[i][2],
        elapsed: Math.round(rows[i][3] / 100) / 10,
        target: rows[i][4] / 1000,
        diff: rows[i][6]
      });
    }
  }

  // 統計
  let avg = 0, min = Infinity, max = -Infinity;
  if (results.length > 0) {
    const diffs = results.map(r => Math.abs(r.diff));
    avg = Math.round(diffs.reduce((a, b) => a + b, 0) / diffs.length * 10) / 10;
    min = Math.round(Math.min(...diffs) * 10) / 10;
    max = Math.round(Math.max(...diffs) * 10) / 10;
  }

  return {
    results: results,
    count: results.length,
    stats: { avgAbsDiff: avg, minAbsDiff: min === Infinity ? 0 : min, maxAbsDiff: max === -Infinity ? 0 : max }
  };
}

function resetSession(data) {
  const sessionId = data.sessionId;

  // sessions をリセット
  const sessions = getOrCreateSheet('sessions');
  const sRows = sessions.getDataRange().getValues();
  for (let i = sRows.length - 1; i >= 1; i--) {
    if (sRows[i][0] === sessionId) {
      sessions.getRange(i + 1, 3).setValue(false);
      sessions.getRange(i + 1, 4).setValue('');
    }
  }

  // waiting をクリア
  const waiting = getOrCreateSheet('waiting');
  const wRows = waiting.getDataRange().getValues();
  for (let i = wRows.length - 1; i >= 1; i--) {
    if (wRows[i][0] === sessionId) {
      waiting.deleteRow(i + 1);
    }
  }

  // results はクリアしない（履歴として残す）

  return { success: true };
}

// ============================================
// アセスメント機能
// ============================================

function saveAssessment(data) {
  const sheet = getOrCreateSheet('assessments');

  // 回答を取得
  const answers = data.answers; // [q1, q2, ..., q20] 各1-5

  // 逆転項目を反転（6:R, 7:R, 8:R, 9:R, 10:R, 15:R, 16:R, 17:R, 18:R, 19:R, 20:R）
  const reverseItems = [6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20];
  const reversed = answers.map((val, idx) => {
    const itemNum = idx + 1;
    if (reverseItems.includes(itemNum)) {
      return 6 - val; // 5段階の反転: 1→5, 2→4, 3→3, 4→2, 5→1
    }
    return val;
  });

  // ビッグファイブ算出
  // E: 1, 6R, 11, 16R → index 0, 5, 10, 15
  // A: 2, 7R, 12, 17R → index 1, 6, 11, 16
  // C: 3, 8R, 13, 18R → index 2, 7, 12, 17
  // N: 4, 9R, 14, 19R → index 3, 8, 13, 18
  // O: 5, 10R, 15R, 20R → index 4, 9, 14, 19
  const E = reversed[0] + reversed[5] + reversed[10] + reversed[15];
  const A = reversed[1] + reversed[6] + reversed[11] + reversed[16];
  const C = reversed[2] + reversed[7] + reversed[12] + reversed[17];
  const N = reversed[3] + reversed[8] + reversed[13] + reversed[18];
  const O = reversed[4] + reversed[9] + reversed[14] + reversed[19];

  // z標準化
  // [SYNC] Norms (Donnellan 2006)。変更時は assessment-result.html の norms も同時に更新すること
  const norms = { E: {mean:11.8, sd:3.9}, A: {mean:14.9, sd:3.1}, C: {mean:13.6, sd:3.4}, N: {mean:10.5, sd:3.7}, O: {mean:14.4, sd:3.2} };
  const z_E = (E - norms.E.mean) / norms.E.sd;
  const z_A = (A - norms.A.mean) / norms.A.sd;
  const z_C = (C - norms.C.mean) / norms.C.sd;
  const z_N = (N - norms.N.mean) / norms.N.sd;
  const z_O = (O - norms.O.mean) / norms.O.sd;

  // スコア計算
  const overScore = 0.50 * z_N + 0.30 * (-z_C) + 0.20 * (-z_E);
  const underScore = 0.45 * z_E + 0.35 * z_O + 0.20 * (-z_N);
  const calibration = z_C;

  // タイプ判定
  // [SYNC] 閾値。変更時は assessment-result.html の THRESHOLD も同時に更新すること
  const THRESHOLD = 0.30;
  let type;
  if (overScore >= THRESHOLD && underScore < THRESHOLD) type = 'over';
  else if (overScore < THRESHOLD && underScore >= THRESHOLD) type = 'under';
  else if (overScore >= THRESHOLD && underScore >= THRESHOLD) type = 'extreme';
  else type = 'mixed';

  // 回答IDを生成
  const responseId = Utilities.getUuid();

  // スプレッドシートに保存
  const row = [
    responseId, data.name || '', data.email || '', data.company || '', data.role || '', data.sessionId || '',
    ...answers,
    E, A, C, N, O,
    Math.round(z_E * 1000) / 1000,
    Math.round(z_A * 1000) / 1000,
    Math.round(z_C * 1000) / 1000,
    Math.round(z_N * 1000) / 1000,
    Math.round(z_O * 1000) / 1000,
    Math.round(overScore * 1000) / 1000,
    Math.round(underScore * 1000) / 1000,
    Math.round(calibration * 1000) / 1000,
    type,
    new Date().toISOString()
  ];
  sheet.appendRow(row);

  // 結果表示ページのURLを返す
  const resultUrl = 'https://shishimaru1231.github.io/time-university/assessment-result.html?e=' + E + '&a=' + A + '&c=' + C + '&n=' + N + '&o=' + O;

  return {
    success: true,
    responseId: responseId,
    scores: { E: E, A: A, C: C, N: N, O: O },
    zScores: {
      E: Math.round(z_E * 100) / 100,
      A: Math.round(z_A * 100) / 100,
      C: Math.round(z_C * 100) / 100,
      N: Math.round(z_N * 100) / 100,
      O: Math.round(z_O * 100) / 100
    },
    overScore: Math.round(overScore * 100) / 100,
    underScore: Math.round(underScore * 100) / 100,
    calibration: Math.round(calibration * 100) / 100,
    type: type,
    resultUrl: resultUrl
  };
}
