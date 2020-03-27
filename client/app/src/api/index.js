import axios from 'axios'

export const getResults = async () => {
  const results = await axios.get('http://127.0.0.1:5000/result')
  return results
}