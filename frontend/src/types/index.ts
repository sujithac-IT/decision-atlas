export interface User {
  id: string
  email: string
  name: string
  createdAt: Date
}

export interface Decision {
  id: string
  title: string
  description: string
  userId: string
  status: 'pending' | 'approved' | 'rejected'
  createdAt: Date
  updatedAt: Date
}

export interface APIResponse<T> {
  success: boolean
  data?: T
  error?: string
  message?: string
}
