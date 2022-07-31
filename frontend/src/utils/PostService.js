import axios from 'axios'

axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

const url = '/post/'

class PostService {
  static async insertAppointment (name, email, tel, date, time) {
    const res = await axios.post(url, {
      name, email, tel, date, time
    })
    return res
  }
}

export default PostService
