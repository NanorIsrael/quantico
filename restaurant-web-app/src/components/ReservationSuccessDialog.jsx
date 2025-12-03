import DialogModal from './DialogModal';
import { useState } from 'react';


const PaymentSuccessfulDialog = () => {
  const  [openModal, setOpenModal] = useState(true)

  return (
    <DialogModal
      size="lg"
      setIsOpen={(value) => {
        setOpenModal(value);
      }}
      isOpen={openModal}
      showActions={true}
      title={"Success"}
      description=""
      triggerComponent={<div></div>}
      content={
        <div>
          <div className="bg-amber-50 border-l-4 border-amber-500 p-6 rounded-lg text-center">
            <h3 className="text-2xl font-semibold text-amber-800 mb-2">Reservation Confirmed!</h3>
            <p className="text-stone-700">
              Thank you for your reservation. We'll send a confirmation email shortly.
            </p>
          </div>
        </div>
      }
    />
  );
};
export default PaymentSuccessfulDialog;
