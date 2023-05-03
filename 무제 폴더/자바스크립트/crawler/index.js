import {
    launch,
    goto,
    checkPopup,
    evalCode,
    evalSigungu,
    closeAlert,
    getPageLength,
    getData,
    writeFile,
} from './module/crawler.js'
import { addressParser } from './module/parser.js';


async function main() {
    console.log('start');

    await launch()

    await goto()

    await checkPopup()

    await evalCode('jeju')

    await evalSigungu('jeju')

    await closeAlert()

    await getPageLength()

    await getData()

    await writeFile()

    console.log('end');
}

main()