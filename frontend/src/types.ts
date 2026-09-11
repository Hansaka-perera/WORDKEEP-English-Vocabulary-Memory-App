export type EnglishType = "American" | "British" | "Both";
export type Difficulty = "Easy" | "Medium" | "Hard" | "Very Hard";
export type MemoryStatus = "New" | "Learning" | "Remembering" | "Strong" | "Forgotten";

export interface Word {
  id: string;
  word: string;
  wordType: string;
  englishType: EnglishType;
  category: string;
  definition: string;
  exampleSentence: string;
  secondExample?: string;
  personalNote?: string;
  difficulty: Difficulty;
  favorite: boolean;
  highlighted: boolean;
  highlightLevel: string;
  memoryStatus: MemoryStatus;
  memoryScore: number;
  reviewCount: number;
  correctCount: number;
  wrongCount: number;
  createdAt: string;
  lastReviewed?: string | null;
  nextReview: string;
}
