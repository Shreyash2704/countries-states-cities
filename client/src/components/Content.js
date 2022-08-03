import React,{useState,useEffect} from 'react'
import { Table } from 'react-bootstrap'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCoffee,faPen,faArrowCircleRight,faInfoCircle} from '@fortawesome/free-solid-svg-icons'
import axios from 'axios'
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';

export default function Content() {
    const [Countries, setCountries] = useState([])
    const [States, setStates] = useState([])
    const [Cities, setCities] = useState([])
    const [allCountries, setallCountries] = useState([])
    const [allStates, setallStates] = useState([])
    const [allCities, setallCities] = useState([])

    

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const [ModelData, setModelData] = useState({})

    const loadCountries = async() =>{
        const api = "http://localhost:8000/countriesApi/country/?format=json"
        const response = await axios.get(api)
        console.log(response.data)
        setCountries(response.data)
        setallCountries(response.data)
    }
    const loadStates = async(country_code) =>{
        const api = `http://localhost:8000/countriesApi/state/${country_code}?format=json`
        const response = await axios.get(api)
        console.log(response.data)
        setStates(response.data)
        setallStates(response.data)
    }
    const loadCities = async(state_code) =>{
        const api = `http://localhost:8000/countriesApi/city/${state_code}?format=json`
        const response = await axios.get(api)
        console.log(response.data)
        setCities(response.data)
        setallCities(response.data)
    }

    const SearchCountry = (country)=>{
        if(country !== ""){
            var arr = []
            allCountries.map(ele=>{
                if(ele.name.includes(country)){
                    arr.push(ele)
                }
            })
            setCountries(arr)
        }
        else{
            setCountries(allCountries)
        }
        
    }
    const SearchState = (state)=>{
        if(state !== ""){
            var arr = []
            allStates.map(ele=>{
                if(ele.name.includes(state)){
                    arr.push(ele)
                }
            })
            setStates(arr)
        }
        else{
            setStates(allStates)
        }
    }
    const SearchCity = (city)=>{
        if(city !== ""){
            var arr = []
            allCities.map(ele=>{
                if(ele.name.includes(city)){
                    arr.push(ele)
                }
            })
            setCities(arr)
        }else{
            setCities(allCities)
        }
        
    }

    const setModel = (data) =>{
        console.log(data)
        setModelData(data)
        handleShow()
    }


    useEffect(() => {
     loadCountries()

    }, [])
    
  return (
    <div className='row p-4'>
        <div className='col-md-4'>
            <Table  bordered>
                <thead>
                    <tr>
                    <th className="px-4 py-2">Countries</th>
                    </tr>
                    <tr>
                    <th className="px-4 py-2">
                        <input type="text" className="form-control" placeholder='Search Country' onChange={(e)=> SearchCountry(e.target.value)}  name="cities" />
                    </th>
                    </tr>
                </thead>
                <tbody>
                    {
                        Countries.length !== 0 && 
                        (
                            Countries.map(ele =>{
                                return(
                                    <tr>
                                        <td className="px-4 py-2 box">
                                            <span className='px-3 name'>{ele.emoji} {ele.name} {ele.iso2}</span>
                                            <span className='px-3 mx-3 infos'>
                                                <a onClick={() => setModel(ele)} className='info'><FontAwesomeIcon icon={faInfoCircle} /> </a>
                                                <a className="arrow" onClick={() => loadStates(ele.iso2)}><FontAwesomeIcon icon={faArrowCircleRight} /></a>
                                            </span>
                                        </td>
                                    </tr>
                                )
                            })
                        )
                    }
                    
                </tbody>
            </Table>
        </div>
        <div className='col-md-4'>
        <Table  bordered>
                <thead>
                    <tr>
                    <th className="px-4 py-2">States</th>
                    </tr>
                    <tr>
                    <th className="px-4 py-2">
                        <input type="text" className="form-control" onChange={(e) => SearchState(e.target.value)} placeholder='Search States' name="cities" />
                    </th>
                    </tr>
                </thead>
                <tbody>
                    {
                        States.length !== 0 &&(
                            States.map(ele=>{
                                return(
                                    <tr>
                                    <td className="px-4 py-2 box">
                                        <span className='px-3 name'> {ele.name} {ele.state_code}</span>
                                        <span className='px-3 mx-3 infos'>
                                            <a onClick={() => setModel(ele)} className='info'><FontAwesomeIcon icon={faInfoCircle} /> </a>
                                            <a className="arrow" onClick={() => loadCities(ele.state_code)}><FontAwesomeIcon icon={faArrowCircleRight} /></a>
                                        </span>
                                    </td>
                                    </tr>
                                )
                            })
                        )
                    }
                    
                </tbody>
            </Table>
        </div>
        <div className='col-md-4'>
        <Table  bordered>
                <thead>
                    <tr>
                    <th className="px-4 py-2">Cities</th>
                    </tr>
                    <tr>
                    <th className="px-4 py-2">
                        <input type="text" className="form-control" onChange={(e) => SearchCity(e.target.value)} placeholder='Search cities' name="cities" />
                    </th>
                    </tr>
                </thead>
                <tbody>
                {
                        Cities.length !== 0 &&(
                            Cities.map(ele=>{
                                return(
                                    <tr>
                                    <td className="px-4 py-2 box">
                                        <span className='px-3 name'> {ele.name} </span>
                                        <span className='px-3 mx-3 infos'>
                                            <a onClick={() => setModel(ele)} className='info'><FontAwesomeIcon icon={faInfoCircle} /> </a>
                                            
                                        </span>
                                    </td>
                                    </tr>
                                )
                            })
                        )
                    }
                </tbody>
            </Table>
        </div>


        <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <Modal.Header closeButton>
          <Modal.Title>{ModelData.name}</Modal.Title>
        </Modal.Header>
        <Modal.Body className="bg-dark text-white mx-3 my-2">
          {ModelData!== {} && (
            <>{JSON.stringify(ModelData,undefined, 2)}</>
          )}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary">Understood</Button>
        </Modal.Footer>
      </Modal>
    </div>
  )
}
