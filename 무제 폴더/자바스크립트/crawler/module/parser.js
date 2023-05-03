import axios from "axios";

async function addressParser (data){

    const res = await axios.get('https://dapi.kakao.com/v2/local/search/address.json',{
        params: {
            query: data.address,
        },
        headers: {
            Authorization: 'KakaoAK 0618f624793b0104c8f4c71f11e46a0a'
        }
    })

    let lng, lat = 0

    if(res.data.documents.length > 0){
        lng = res.data.documents[0].address.x
        lat = res.data.documents[0].address.y
    }

    data.lng = Number(lng)
    data.lat = Number(lat)

    return data
}

export { addressParser}