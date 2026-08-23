import assert from 'node:assert';
import { calculateBraSize, validateAndCalculateBraSize, convertKnownSize, calculateSisterSizes, BAND_CONVERSION_MATRIX, CUP_CONVERSION_MATRIX } from '../src/utils/braSizing.js';

console.log('🧪 Running Bra Sizing Methodology, Conversion & Validation Test Suite...\n');

let passedTests = 0;
let totalTests = 0;

function runTest(name: string, fn: () => void) {
  totalTests++;
  try {
    fn();
    passedTests++;
    console.log(`  ✓ ${name}`);
  } catch (err) {
    console.error(`  ✕ ${name}`);
    console.error(err);
    process.exitCode = 1;
  }
}

// 1. Normal Measurements (Inches)
runTest('Normal Measurement 32" underbust, 35" bust -> 32C', () => {
  const result = calculateBraSize({ underbust: 32, overbust: 35, unit: 'in' });
  assert.ok(result !== null);
  assert.strictEqual(result.primarySize, '32C');
  assert.strictEqual(result.sisterTight, '30D');
  assert.strictEqual(result.sisterLoose, '34B');
});

runTest('Normal Measurement 34" underbust, 37" bust -> 34C', () => {
  const result = calculateBraSize({ underbust: 34, overbust: 37, unit: 'in' });
  assert.ok(result !== null);
  assert.strictEqual(result.primarySize, '34C');
  assert.strictEqual(result.sisterTight, '32D');
  assert.strictEqual(result.sisterLoose, '36B');
});

// 2. Small Measurements
runTest('Small Measurement 28" underbust, 29" bust -> 28A', () => {
  const result = calculateBraSize({ underbust: 28, overbust: 29, unit: 'in' });
  assert.ok(result !== null);
  assert.strictEqual(result.primarySize, '28A');
  assert.strictEqual(result.sisterTight, '26B');
  assert.strictEqual(result.sisterLoose, '30AA');
});

// 3. Large Measurements
runTest('Large Measurement 40" underbust, 48" bust -> 40FF (UK) / 40H (US)', () => {
  const result = calculateBraSize({ underbust: 40, overbust: 48, unit: 'in' });
  assert.ok(result !== null);
  assert.strictEqual(result.primarySize, '40H');
  const ukEntry = result.internationalSizes.find(s => s.location === 'UK' && !s.isSecondary);
  assert.strictEqual(ukEntry?.cup, 'FF');
});

// 4. Decimal Measurements
runTest('Decimal Measurement 31.4" underbust, 35.2" bust -> 32C', () => {
  const result = calculateBraSize({ underbust: 31.4, overbust: 35.2, unit: 'in' });
  assert.ok(result !== null);
  assert.strictEqual(result.primarySize, '32C');
});

// 5. Centimeter Input Conversion
runTest('Centimeter Input (80 cm underbust, 95 cm bust) -> EU 80B, FR 95B', () => {
  const result = calculateBraSize({ underbust: 80, overbust: 95, unit: 'cm' });
  assert.ok(result !== null);
  const euEntry = result.internationalSizes.find(s => s.location === 'EU (EN 13402)');
  const frEntry = result.internationalSizes.find(s => s.location === 'FR / BE / ES');
  assert.strictEqual(euEntry?.band, '80 cm');
  assert.strictEqual(euEntry?.cup, 'B');
  assert.strictEqual(frEntry?.band, '95 cm');
  assert.strictEqual(frEntry?.cup, 'B');
});

// 6. International Conversions (US, UK, EU, FR, AU, JP)
runTest('All International Conversions for 34" / 37" (34C)', () => {
  const result = calculateBraSize({ underbust: 34, overbust: 37, unit: 'in' });
  assert.ok(result !== null);
  const us = result.internationalSizes.find(s => s.location === 'US / CA');
  const uk = result.internationalSizes.find(s => s.location === 'UK');
  const eu = result.internationalSizes.find(s => s.location === 'EU (EN 13402)');
  const fr = result.internationalSizes.find(s => s.location === 'FR / BE / ES');
  const au = result.internationalSizes.find(s => s.location === 'Australia / New Zealand');
  const jp = result.internationalSizes.find(s => s.location === 'Japan (JP)');

  assert.strictEqual(us?.band, '34');
  assert.strictEqual(us?.cup, 'C');
  assert.strictEqual(uk?.band, '34');
  assert.strictEqual(uk?.cup, 'C');
  assert.strictEqual(eu?.band, '85 cm');
  assert.strictEqual(fr?.band, '100 cm');
  assert.strictEqual(au?.band, '12');
  assert.strictEqual(jp?.band, '85');
  assert.strictEqual(jp?.cup, 'AA');
});

// 7. Conversion Matrix Integrity & Bi-directional Lookup
runTest('Conversion Matrix Consistency (BAND & CUP matrices)', () => {
  assert.strictEqual(BAND_CONVERSION_MATRIX.length, 6);
  assert.strictEqual(CUP_CONVERSION_MATRIX.length, 10);

  // Check 34 band row
  const row34 = BAND_CONVERSION_MATRIX.find(r => r.us === 34);
  assert.strictEqual(row34?.uk, 34);
  assert.strictEqual(row34?.eu, 75);
  assert.strictEqual(row34?.fr, 90);
  assert.strictEqual(row34?.au, 12);
  assert.strictEqual(row34?.jp, 75);

  // Check DD cup row
  const rowDD = CUP_CONVERSION_MATRIX.find(r => r.uk === 'DD');
  assert.strictEqual(rowDD?.us, 'DD / E');
  assert.strictEqual(rowDD?.eu, 'E');
  assert.strictEqual(rowDD?.au, 'DD');
  assert.strictEqual(rowDD?.jp, 'E');
});

// 8. Known Size Converter Function (convertKnownSize)
runTest('Known Size Converter Function (convertKnownSize)', () => {
  // US 34C -> UK 34C, EU 75C, FR 90C, AU 12C, JP 75C
  const conv34C = convertKnownSize('US', 34, 'C');
  assert.ok(conv34C !== null);
  assert.strictEqual(conv34C.us.full, '34C');
  assert.strictEqual(conv34C.uk.full, '34C');
  assert.strictEqual(conv34C.eu.full, '75C');
  assert.strictEqual(conv34C.fr.full, '90C');
  assert.strictEqual(conv34C.au.full, '12C');
  assert.strictEqual(conv34C.jp.full, '75C');

  // UK 32FF -> US 32H, EU 70H, FR 85H, AU 10FF, JP 70H
  const conv32FF = convertKnownSize('UK', 32, 'FF');
  assert.ok(conv32FF !== null);
  assert.strictEqual(conv32FF.us.full, '32H');
  assert.strictEqual(conv32FF.uk.full, '32FF');
  assert.strictEqual(conv32FF.eu.full, '70H');
  assert.strictEqual(conv32FF.fr.full, '85H');
  assert.strictEqual(conv32FF.au.full, '10FF');
  assert.strictEqual(conv32FF.jp.full, '70H');

  // Invalid lookup
  assert.strictEqual(convertKnownSize('US', 99, 'Z'), null);
});

// 9. Sister Size Calculator Function (calculateSisterSizes)
runTest('Sister Size Calculator Function (calculateSisterSizes)', () => {
  const sisters34C = calculateSisterSizes(34, 'C');
  assert.ok(sisters34C !== null);
  assert.strictEqual(sisters34C.currentSize, '34C');
  assert.strictEqual(sisters34C.sisterTight, '32D');
  assert.strictEqual(sisters34C.sisterLoose, '36B');

  const sisters32D = calculateSisterSizes(32, 'D');
  assert.ok(sisters32D !== null);
  assert.strictEqual(sisters32D.currentSize, '32D');
  assert.strictEqual(sisters32D.sisterTight, '30DD');
  assert.strictEqual(sisters32D.sisterLoose, '34C');

  assert.strictEqual(calculateSisterSizes(10, 'Z'), null);
});

// 10. Invalid & Boundary Measurements
runTest('Invalid Measurements (Zero, Negative, or Bust < Underbust)', () => {
  assert.strictEqual(calculateBraSize({ underbust: 0, overbust: 34, unit: 'in' }), null);
  assert.strictEqual(calculateBraSize({ underbust: 34, overbust: -5, unit: 'in' }), null);
  assert.strictEqual(calculateBraSize({ underbust: 34, overbust: 30, unit: 'in' }), null);
  assert.strictEqual(calculateBraSize({ underbust: NaN, overbust: 34, unit: 'in' }), null);
});

// 11. Input Validation & Error Handling Tests
runTest('Validation Error Handling (validateAndCalculateBraSize)', () => {
  // Test zero / negative
  const zeroRes = validateAndCalculateBraSize({ underbust: 0, overbust: 34, unit: 'in' });
  assert.strictEqual(zeroRes.isValid, false);
  assert.strictEqual(zeroRes.error, 'Band size must be greater than zero.');

  // Test absurd numbers (999)
  const absurdRes = validateAndCalculateBraSize({ underbust: 34, overbust: 999, unit: 'in' });
  assert.strictEqual(absurdRes.isValid, false);
  assert.strictEqual(absurdRes.error, 'Please enter a bust size between 22 and 80 inches.');

  // Test bust < underbust
  const invalidOrderRes = validateAndCalculateBraSize({ underbust: 36, overbust: 32, unit: 'in' });
  assert.strictEqual(invalidOrderRes.isValid, false);
  assert.strictEqual(invalidOrderRes.error, 'Bust size must be equal to or larger than band size.');

  // Test valid calculation
  const validRes = validateAndCalculateBraSize({ underbust: 34, overbust: 37, unit: 'in' });
  assert.strictEqual(validRes.isValid, true);
  assert.strictEqual(validRes.result?.primarySize, '34C');
});

console.log(`\n🎉 Results: ${passedTests} / ${totalTests} test cases passed successfully!\n`);
