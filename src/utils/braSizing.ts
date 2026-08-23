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

export const US_CUPS = ['AA', 'A', 'B', 'C', 'D', 'DD', 'DDD', 'G', 'H', 'I', 'J', 'K', 'L'];
export const UK_CUPS = ['AA', 'A', 'B', 'C', 'D', 'DD', 'E', 'F', 'FF', 'G', 'GG', 'H', 'HH', 'J'];
export const EU_CUPS = ['AA', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'];

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
  let auBand = usBand - 22;
  if (auBand < 4) auBand = 4;
  const auCup = ukCup;

  // --- Japan (JP) ---
  let jpBand = euBand;
  const jpCup = euCup;

  // --- Sister Sizes (US) ---
  const tightBand = Math.max(usBand - 2, 28);
  const tightCupIndex = Math.min(usDiff + 1, US_CUPS.length - 1);
  const tightSize = `${tightBand}${US_CUPS[tightCupIndex]}`;

  const looseBand = usBand + 2;
  const looseCupIndex = Math.max(usDiff - 1, 0);
  const looseSize = `${looseBand}${US_CUPS[looseCupIndex]}`;

  const primarySize = `${usBand}${usCup}`;

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
