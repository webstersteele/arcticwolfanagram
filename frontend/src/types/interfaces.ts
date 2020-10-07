export interface ITablePair{
    words: [string, string]
    frequency: number
}

export interface IFormPair {
    word1: string,
    word2: string
}

export interface IFormProp {
    isLoading: boolean,
    isSubmitted: boolean,
    isAnagram: boolean
    onSubmit: (data: IFormPair) => void
}

export interface ITableProp {
    anagramList: ITablePair[]
}