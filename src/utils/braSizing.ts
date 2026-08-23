export interface BraSizeInput {
  underbust: number;
  overbust: number;
  unit: 'in' | 'cm';
}

export interface InternationalSize {
  location: string;
  band: string;
  cup: string;
  isSecondary?: boolean;
}

export interface BraSizeResult {
  primarySize: string;
  usBand: number;
  usCup: string;
  sisterTight: string;
  sisterLoose: string;
  internationalSizes: InternationalSize[];
}

export interface BraValidationResponse {
  isValid: boolean;
  error?: string;
  fieldWithError?: 'underbust' | 'overbust' | 'both';
  result?: BraSizeResult;
}

export interface BandRow {
  us: number;
  uk: number;
  eu: number;
  fr: number;
  au: number;
  jp: number;
}

export interface CupRow {
  us: string;
  uk: string;
  eu: string;
  au: string;
  jp: string;
}

export const US_CUPS = ['AA', 'A', 'B', 'C', 'D', 'DD', 'DDD', 'G', 'H', 'I', 'J', 'K', 'L'];
export const UK_CUPS = ['AA', 'A', 'B', 'C', 'D', 'DD', 'E', 'F', 'FF', 'G', 'GG', 'H', 'HH', 'J'];
export const EU_CUPS = ['AA', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'];

export const BAND_CONVERSION_MATRIX: BandRow[] = [
  { us: 30, uk: 30, eu: 65, fr: 80, au: 8, jp: 65 },
  { us: 32, uk: 32, eu: 70, fr: 85, au: 10, jp: 70 },
  { us: 34, uk: 34, eu: 75, fr: 90, au: 12, jp: 75 },
  { us: 36, uk: 36, eu: 80, fr: 95, au: 14, jp: 80 },
  { us: 38, uk: 38, eu: 85, fr: 100, au: 16, jp: 85 },
  { us: 40, uk: 40, eu: 90, fr: 105, au: 18, jp: 90 },
];

export const CUP_CONVERSION_MATRIX: CupRow[] = [
  { us: 'A', uk: 'A', eu: 'A', au: 'A', jp: 'A' },
  { us: 'B', uk: 'B', eu: 'B', au: 'B', jp: 'B' },
  { us: 'C', uk: 'C', eu: 'C', au: 'C', jp: 'C' },
  { us: 'D', uk: 'D', eu: 'D', au: 'D', jp: 'D' },
  { us: 'DD / E', uk: 'DD', eu: 'E', au: 'DD', jp: 'E' },
  { us: 'DDD / F', uk: 'E', eu: 'F', au: 'E', jp: 'F' },
  { us: 'G', uk: 'F', eu: 'G', au: 'F', jp: 'G' },
  { us: 'H', uk: 'FF', eu: 'H', au: 'FF', jp: 'H' },
  { us: 'I', uk: 'G', eu: 'I', au: 'G', jp: 'I' },
  { us: 'J', uk: 'GG', eu: 'J', au: 'GG', jp: 'J' },
];

/**
 * Validates inputs and calculates bra size, returning structured error messages if invalid.
 */
export function validateAndCalculateBraSize(input: BraSizeInput): BraValidationResponse {
  const { underbust, overbust, unit } = input;

  if (typeof underbust !== 'number' || isNaN(underbust) || !isFinite(underbust)) {
    return { isValid: false, error: 'Please enter a valid numeric band size.', fieldWithError: 'underbust' };
  }
  if (typeof overbust !== 'number' || isNaN(overbust) || !isFinite(overbust)) {
    return { isValid: false, error: 'Please enter a valid numeric bust size.', fieldWithError: 'overbust' };
  }

  if (underbust <= 0) {
    return { isValid: false, error: 'Band size must be greater than zero.', fieldWithError: 'underbust' };
  }
  if (overbust <= 0) {
    return { isValid: false, error: 'Bust size must be greater than zero.', fieldWithError: 'overbust' };
  }

  if (unit === 'in') {
    if (underbust < 20 || underbust > 60) {
      return { isValid: false, error: 'Please enter a band size between 20 and 60 inches.', fieldWithError: 'underbust' };
    }
    if (overbust < 22 || overbust > 80) {
      return { isValid: false, error: 'Please enter a bust size between 22 and 80 inches.', fieldWithError: 'overbust' };
    }
  } else {
    if (underbust < 50 || underbust > 150) {
      return { isValid: false, error: 'Please enter a band size between 50 and 150 cm.', fieldWithError: 'underbust' };
    }
    if (overbust < 55 || overbust > 200) {
      return { isValid: false, error: 'Please enter a bust size between 55 and 200 cm.', fieldWithError: 'overbust' };
    }
  }

  if (overbust < underbust) {
    return { isValid: false, error: 'Bust size must be equal to or larger than band size.', fieldWithError: 'overbust' };
  }

  const result = calculateBraSize(input);
  if (!result) {
    return { isValid: false, error: 'Unable to calculate bra size with provided measurements.' };
  }

  return { isValid: true, result };
}

/**
 * Calculates bra size recommendations based on bust and underbust measurements.
 */
export function calculateBraSize(input: BraSizeInput): BraSizeResult | null {
  const { underbust, overbust, unit } = input;

  if (
    typeof underbust !== 'number' ||
    typeof overbust !== 'number' ||
    isNaN(underbust) ||
    isNaN(overbust) ||
    !isFinite(underbust) ||
    !isFinite(overbust) ||
    underbust <= 0 ||
    overbust <= 0 ||
    overbust < underbust
  ) {
    return null;
  }

  // Convert to inches and cm
  let u_in = unit === 'cm' ? underbust / 2.54 : underbust;
  let o_in = unit === 'cm' ? overbust / 2.54 : overbust;
  let u_cm = unit === 'cm' ? underbust : underbust * 2.54;
  let o_cm = unit === 'cm' ? overbust : overbust * 2.54;

  // --- US/CA & UK (Modern Direct Underbust Sizing) ---
  let usBand = Math.round(u_in);
  if (usBand % 2 !== 0) usBand += 1;
  if (usBand < 28) usBand = 28;

  let usDiff = Math.round(o_in - usBand);
  if (usDiff < 0) usDiff = 0;

  const usCupIndex = Math.min(usDiff, US_CUPS.length - 1);
  const ukCupIndex = Math.min(usDiff, UK_CUPS.length - 1);

  const usCup = US_CUPS[usCupIndex];
  const ukCup = UK_CUPS[ukCupIndex];

  // --- US/CA & UK (Traditional Underbust +4 Sizing) ---
  let u_round = Math.round(u_in);
  let plus4Band = u_round % 2 === 0 ? u_round + 4 : u_round + 5;
  let plus4Diff = Math.round(o_in - plus4Band);
  if (plus4Diff < 0) plus4Diff = 0;

  const plus4UsCup = US_CUPS[Math.min(plus4Diff, US_CUPS.length - 1)];
  const plus4UkCup = UK_CUPS[Math.min(plus4Diff, UK_CUPS.length - 1)];

  // --- EU (EN 13402) ---
  let euBand = Math.round(u_cm / 5) * 5;
  if (euBand < 60) euBand = 60;
  let euDiff = o_cm - u_cm;
  let euCupIndex = Math.floor((euDiff - 10) / 2);
  if (euCupIndex < 0) euCupIndex = 0;
  const euCup = EU_CUPS[Math.min(euCupIndex, EU_CUPS.length - 1)];

  // --- FR / BE / ES ---
  let frBand = euBand + 15;

  // --- Australia / New Zealand ---
  let auBand = 8 + (usBand - 30);
  if (auBand < 6) auBand = 6;
  const auCup = ukCup;

  // --- Japan (JP) ---
  let jpBand = euBand;
  const jpCup = euCup;

  const primarySize = `${usBand}${usCup}`;
  const tightSize = `${usBand - 2}${US_CUPS[Math.min(usCupIndex + 1, US_CUPS.length - 1)]}`;
  const looseSize = `${usBand + 2}${US_CUPS[Math.max(usCupIndex - 1, 0)]}`;

  const internationalSizes: InternationalSize[] = [
    { location: 'US / CA', band: `${usBand}`, cup: usCup },
    { location: 'UK', band: `${usBand}`, cup: ukCup },
    { location: 'US / CA (Underbust +4)*', band: `${plus4Band}`, cup: plus4UsCup, isSecondary: true },
    { location: 'UK (Underbust +4)*', band: `${plus4Band}`, cup: plus4UkCup, isSecondary: true },
    { location: 'EU (EN 13402)', band: `${euBand} cm`, cup: euCup },
    { location: 'FR / BE / ES', band: `${frBand} cm`, cup: euCup },
    { location: 'Australia / New Zealand', band: `${auBand}`, cup: auCup },
    { location: 'Japan (JP)', band: `${jpBand}`, cup: jpCup },
  ];

  return {
    primarySize,
    usBand,
    usCup,
    sisterTight: tightSize,
    sisterLoose: looseSize,
    internationalSizes,
  };
}

export interface ConvertKnownSizeResult {
  us: { band: number; cup: string; full: string };
  uk: { band: number; cup: string; full: string };
  eu: { band: number; cup: string; full: string };
  fr: { band: number; cup: string; full: string };
  au: { band: number; cup: string; full: string };
  jp: { band: number; cup: string; full: string };
}

/**
 * Converts a known bra size from one system to all supported international systems using authoritative matrices.
 */
export function convertKnownSize(
  systemKey: 'US' | 'UK' | 'EU' | 'FR' | 'AU' | 'JP',
  bandVal: number,
  cupVal: string
): ConvertKnownSizeResult | null {
  const key = systemKey.toLowerCase() as keyof BandRow;

  // Match Band row
  const bandRowIndex = BAND_CONVERSION_MATRIX.findIndex(row => row[key] === bandVal);
  if (bandRowIndex === -1) return null;
  const bandRow = BAND_CONVERSION_MATRIX[bandRowIndex];

  // Match Cup row
  const cupKey = (systemKey === 'FR' ? 'eu' : key) as keyof CupRow;
  const cupRowIndex = CUP_CONVERSION_MATRIX.findIndex(row => {
    const val = row[cupKey];
    if (typeof val === 'string') {
      return val.split('/').map(s => s.trim().toLowerCase()).includes(cupVal.trim().toLowerCase());
    }
    return false;
  });
  if (cupRowIndex === -1) return null;
  const cupRow = CUP_CONVERSION_MATRIX[cupRowIndex];

  // Clean display cup names
  const cleanCup = (cStr: string) => cStr.split('/')[0].trim();

  return {
    us: { band: bandRow.us, cup: cleanCup(cupRow.us), full: `${bandRow.us}${cleanCup(cupRow.us)}` },
    uk: { band: bandRow.uk, cup: cleanCup(cupRow.uk), full: `${bandRow.uk}${cleanCup(cupRow.uk)}` },
    eu: { band: bandRow.eu, cup: cleanCup(cupRow.eu), full: `${bandRow.eu}${cleanCup(cupRow.eu)}` },
    fr: { band: bandRow.fr, cup: cleanCup(cupRow.eu), full: `${bandRow.fr}${cleanCup(cupRow.eu)}` },
    au: { band: bandRow.au, cup: cleanCup(cupRow.au), full: `${bandRow.au}${cleanCup(cupRow.au)}` },
    jp: { band: bandRow.jp, cup: cleanCup(cupRow.jp), full: `${bandRow.jp}${cleanCup(cupRow.jp)}` },
  };
}

export interface SisterSizesResult {
  currentSize: string;
  sisterTight: string;
  sisterLoose: string;
}

/**
 * Calculates sister sizes for a given baseline band and cup size.
 */
export function calculateSisterSizes(bandVal: number, cupVal: string): SisterSizesResult | null {
  const usCupIndex = US_CUPS.findIndex(c => c.toLowerCase() === cupVal.trim().toLowerCase());
  if (usCupIndex === -1 || bandVal < 26 || bandVal > 56) return null;

  const currentSize = `${bandVal}${US_CUPS[usCupIndex]}`;
  const tightBand = bandVal - 2;
  const tightCupIndex = Math.min(usCupIndex + 1, US_CUPS.length - 1);
  const sisterTight = `${tightBand}${US_CUPS[tightCupIndex]}`;

  const looseBand = bandVal + 2;
  const looseCupIndex = Math.max(usCupIndex - 1, 0);
  const sisterLoose = `${looseBand}${US_CUPS[looseCupIndex]}`;

  return {
    currentSize,
    sisterTight,
    sisterLoose,
  };
}
