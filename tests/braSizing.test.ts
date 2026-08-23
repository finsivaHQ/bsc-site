import assert from 'node:assert';
import { calculateBraSize } from '../src/utils/braSizing.js';

console.log('🧪 Running Bra Sizing Methodology Test Suite...\n');

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
  assert.strictEqual(result.sisterTight, '28B');
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
  assert.strictEqual(eu?.band, '85 cm'); // 34" * 2.54 = 86.36 cm -> rounded to 85 cm
  assert.strictEqual(fr?.band, '100 cm'); // 85 + 15 = 100 cm
  assert.strictEqual(au?.band, '12'); // 34 - 22 = 12
  assert.strictEqual(jp?.band, '85');
  assert.strictEqual(jp?.cup, 'AA');
});

// 7. Invalid & Boundary Measurements
runTest('Invalid Measurements (Zero, Negative, or Bust < Underbust)', () => {
  assert.strictEqual(calculateBraSize({ underbust: 0, overbust: 34, unit: 'in' }), null);
  assert.strictEqual(calculateBraSize({ underbust: 34, overbust: -5, unit: 'in' }), null);
  assert.strictEqual(calculateBraSize({ underbust: 34, overbust: 30, unit: 'in' }), null);
  assert.strictEqual(calculateBraSize({ underbust: NaN, overbust: 34, unit: 'in' }), null);
});

console.log(`\n🎉 Results: ${passedTests} / ${totalTests} test cases passed successfully!\n`);
